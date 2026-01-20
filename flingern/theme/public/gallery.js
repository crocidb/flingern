let setupGalleries = function() {
    const config = window.FLINGERN_CONFIG || {
        galleryColumnsDesktop: 4,
        galleryColumnsMobile: 2,
        galleryBreakpoint: 1200
    };

    document.querySelectorAll('.gallery-object').forEach((placeholder) => {
        let galleryName = placeholder.getAttribute('data-gallery');
        let imageContainer = document.querySelector(`.gallery-images[data-gallery="${galleryName}"]`);

        if (!imageContainer) return;

        let images = Array.from(imageContainer.querySelectorAll('a'));
        if (images.length === 0) return;

        placeholder._galleryImages = images;
        placeholder._galleryConfig = config;

        renderGallery(placeholder);
    });

    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            document.querySelectorAll('.gallery-object').forEach((placeholder) => {
                if (placeholder._galleryImages) {
                    renderGallery(placeholder);
                }
            });
        }, 150);
    });
};

function renderGallery(placeholder) {
    const config = placeholder._galleryConfig;
    const images = placeholder._galleryImages;

    const columnCount = window.innerWidth >= config.galleryBreakpoint
        ? config.galleryColumnsDesktop
        : config.galleryColumnsMobile;

    placeholder.innerHTML = '';

    const container = document.createElement('div');
    container.className = 'container text-center';

    const row = document.createElement('div');
    row.className = 'row align-items-start';

    const columns = [];
    const columnHeights = [];
    for (let i = 0; i < columnCount; i++) {
        const col = document.createElement('div');
        col.className = 'col';
        row.appendChild(col);
        columns.push(col);
        columnHeights.push(0);
    }

    container.appendChild(row);
    placeholder.appendChild(container);

    images.forEach((imgLink) => {
        const clone = imgLink.cloneNode(true);

        // Get actual thumbnail height from data attribute
        const thumbHeight = parseInt(imgLink.getAttribute('data-thumb-height')) || 200;

        // Find shortest column
        let shortestIndex = 0;
        let shortestHeight = columnHeights[0];
        for (let i = 1; i < columnHeights.length; i++) {
            if (columnHeights[i] < shortestHeight) {
                shortestHeight = columnHeights[i];
                shortestIndex = i;
            }
        }

        columns[shortestIndex].appendChild(clone);
        columnHeights[shortestIndex] += thumbHeight;
    });
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupGalleries);
} else {
    setupGalleries();
}
