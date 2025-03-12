// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Add animation to elements on scroll
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.card, .section-title, .profile-image');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (elementPosition < screenPosition) {
                element.classList.add('animate__animated', 'animate__fadeInUp');
            }
        });
    };
    
    // Call the animation function on scroll
    window.addEventListener('scroll', animateOnScroll);
    
    // Call it once on page load
    animateOnScroll();
    
    // Gallery image click to show larger version (simple lightbox effect)
    const galleryItems = document.querySelectorAll('.gallery-item img');
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const src = this.getAttribute('src');
            const alt = this.getAttribute('alt');
            
            const modal = document.createElement('div');
            modal.classList.add('modal', 'fade');
            modal.setAttribute('tabindex', '-1');
            modal.innerHTML = `
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">${alt}</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body p-0">
                            <img src="${src}" class="img-fluid" alt="${alt}">
                        </div>
                    </div>
                </div>
            `;
            
            document.body.appendChild(modal);
            const modalInstance = new bootstrap.Modal(modal);
            modalInstance.show();
            
            modal.addEventListener('hidden.bs.modal', function() {
                document.body.removeChild(modal);
            });
        });
    });
    
    // Booking form calculation (for demonstration)
    const visitorsSelect = document.getElementById('visitors');
    const guideServiceCheck = document.getElementById('guideService');
    
    if (visitorsSelect && guideServiceCheck) {
        const calculateTotal = () => {
            const visitors = parseInt(visitorsSelect.value);
            const withGuide = guideServiceCheck.checked;
            
            let total = visitors * 25000; // Biaya masuk per orang
            if (withGuide) {
                total += 100000; // Biaya layanan pemandu
            }
            
            // Update total if there's an element to show it
            const totalElement = document.getElementById('totalPrice');
            if (totalElement) {
                totalElement.textContent = `Rp ${total.toLocaleString('id-ID')}`;
            }
        };
        
        visitorsSelect.addEventListener('change', calculateTotal);
        guideServiceCheck.addEventListener('change', calculateTotal);
        
        // Initial calculation
        calculateTotal();
    }
}); 