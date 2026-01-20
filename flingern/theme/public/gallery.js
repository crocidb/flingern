let setupGalleries = function() {
    document.querySelectorAll('.gallery-placeholder').forEach((placeholder) => {
        let galleryName = placeholder.getAttribute('data-gallery');
        let imageContainer = document.querySelector(`.gallery-images[data-gallery="${galleryName}"]`);

        if (!imageContainer) return;

        let images = Array.from(imageContainer.querySelectorAll('a'));
        if (images.length === 0) return;

        // Create responsive grid structure
        let desktopGrid = document.createElement('div');
        desktopGrid.className = 'container text-center gallery-desktop';
        desktopGrid.innerHTML = `
            <div class="row align-items-start">
                <div class="col"></div>
                <div class="col"></div>
                <div class="col"></div>
                <div class="col"></div>
            </div>
        `;

        let mobileGrid = document.createElement('div');
        mobileGrid.className = 'container text-center gallery-mobile d-none';
        mobileGrid.innerHTML = `
            <div class="row align-items-start">
                <div class="col"></div>
                <div class="col"></div>
            </div>
        `;

        let distributeImages = function(grid, imgs) {
            let columns = grid.querySelector('.row').children;
            let imagesCopy = imgs.map(x => x.cloneNode(true));
            imagesCopy.reverse();

            while (imagesCopy.length > 0) {
                for (let i = 0; i < columns.length && imagesCopy.length > 0; i++) {
                    let img = imagesCopy.pop();
                    if (img) columns[i].appendChild(img);
                }
            }
        };

        distributeImages(desktopGrid, images);
        distributeImages(mobileGrid, images);

        placeholder.appendChild(desktopGrid);
        placeholder.appendChild(mobileGrid);

        let updateVisibility = function() {
            if (window.innerWidth >= 1200) {
                mobileGrid.classList.add('d-none');
                desktopGrid.classList.remove('d-none');
            } else {
                mobileGrid.classList.remove('d-none');
                desktopGrid.classList.add('d-none');
            }
        };

        updateVisibility();
        window.addEventListener('resize', updateVisibility);
    });
};

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupGalleries);
} else {
    setupGalleries();
}
