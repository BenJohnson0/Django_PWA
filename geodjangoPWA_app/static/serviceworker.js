// serviceworker.js

const VERSION = '{{ version }}';
const staticCachePrefix = 'static';
const staticCacheName = `${staticCachePrefix}-${VERSION}`;
const dynamicCacheName = 'dynamic';

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                console.log('[SW] Caching app shell');
                const urlsToCache = [
                    '/static/manifest.json',
                    '/offline/',
                    '/map/',
                    '/login/',
                    'icons/bus_icon.png',
                    'icons/train_icon.png',
                ];

                // Use Promise.allSettled to handle individual request failures
                return Promise.allSettled(urlsToCache.map(url => cache.add(url)))
                    .then(results => {
                        results.forEach((result, index) => {
                            if (result.status === 'rejected') {
                                console.error(`[SW] Failed to cache: ${urlsToCache[index]}`);
                            }
                        });
                    });
            }),
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith(staticCachePrefix)))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        }),
    );
});

self.addEventListener('fetch', (event) => {
    if (event.request.method !== 'GET') {
        return;
    }

    if (!event.request.url.startsWith('http')) {
        return;
    }

    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) {
                    console.log(`[SW] Served response to ${event.request.url} from the cache.`);
                    return response;
                }

                return fetch(event.request)
                    .then(res => {
                        const responseToCache = res.clone();
                        caches.open(dynamicCacheName)
                            .then(cache => cache.put(event.request, responseToCache))
                            .catch(err => console.warn('[SW] Cache put error:', err));
                        return res;
                    })
                    .catch(err => {
                        console.warn('[SW] Network request failed, app is probably offline', err);
                        return caches.open(staticCacheName)
                            .then((cache) => {
                                if (event.request.headers.get('accept').includes('text/html')) {
                                    return cache.match('/offline/');
                                }
                                return Promise.reject();
                            })
                            .catch(err => console.warn('[SW] Failed to get response from network and cache.', err));
                    });
            })
    );
});


