// Main JavaScript - CGMH Burn Center v2

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded'); // Debug log
    
    // Wait a bit more to ensure all elements are ready
    setTimeout(function() {
        initializeMobileMenu();
    }, 100);
});

// Mobile Menu Initialization
function initializeMobileMenu() {
    console.log('Initializing mobile menu...'); // Debug log
    
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mobileNav = document.querySelector('.mobile-nav');
    
    console.log('Mobile menu elements:', { btn: mobileMenuBtn, nav: mobileNav }); // Debug log
    
    if (mobileMenuBtn && mobileNav) {
        console.log('Setting up mobile menu event listeners'); // Debug log
        
        mobileMenuBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            console.log('Mobile menu button clicked!'); // Debug log
            console.log('Current classes:', mobileNav.className); // Debug log
            
            const isActive = mobileNav.classList.contains('active');
            console.log('Is currently active:', isActive); // Debug log
            
            if (isActive) {
                mobileNav.classList.remove('active');
                console.log('Removed active class'); // Debug log
            } else {
                mobileNav.classList.add('active');
                console.log('Added active class'); // Debug log
            }
            
            // Toggle hamburger animation
            const icon = this.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-times');
                console.log('Toggled icon classes:', icon.className); // Debug log
            }
        });
        
        // Initialize submenu toggles
        initializeSubmenuToggles();
        
        console.log('Mobile menu initialized successfully'); // Debug log
    } else {
        console.error('Mobile menu elements not found!', { btn: mobileMenuBtn, nav: mobileNav });
    }
}

// Initialize submenu toggle functionality
function initializeSubmenuToggles() {
    const submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');
    
    console.log('Found submenu toggles:', submenuToggles.length); // Debug log
    
    submenuToggles.forEach(toggle => {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            console.log('Submenu toggle clicked'); // Debug log
            
            // Find the submenu for this toggle
            const menuItem = this.closest('.mobile-menu-item');
            const submenu = menuItem.querySelector('.mobile-submenu');
            const icon = this.querySelector('i');
            
            if (submenu) {
                // Toggle the submenu
                const isActive = submenu.classList.contains('active');
                
                // Close all other submenus
                document.querySelectorAll('.mobile-submenu.active').forEach(otherSubmenu => {
                    if (otherSubmenu !== submenu) {
                        otherSubmenu.classList.remove('active');
                        const otherToggle = otherSubmenu.closest('.mobile-menu-item').querySelector('.mobile-submenu-toggle');
                        if (otherToggle) {
                            otherToggle.classList.remove('active');
                        }
                    }
                });
                
                // Close all other toggle buttons
                document.querySelectorAll('.mobile-submenu-toggle.active').forEach(otherToggle => {
                    if (otherToggle !== this) {
                        otherToggle.classList.remove('active');
                    }
                });
                
                // Toggle current submenu
                if (isActive) {
                    submenu.classList.remove('active');
                    this.classList.remove('active');
                    console.log('Closed submenu'); // Debug log
                } else {
                    submenu.classList.add('active');
                    this.classList.add('active');
                    console.log('Opened submenu'); // Debug log
                }
            }
        });
    });
}

// Initialize other functionality
document.addEventListener('DOMContentLoaded', function() {
    
    // Close mobile menu when clicking outside
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    
    document.addEventListener('click', function(e) {
        if (mobileNav && !e.target.closest('.header') && !e.target.closest('.mobile-nav')) {
            mobileNav.classList.remove('active');
            const icon = mobileMenuBtn?.querySelector('i');
            if (icon) {
                icon.classList.add('fa-bars');
                icon.classList.remove('fa-times');
            }
        }
    });
    
    // Close mobile menu when clicking on links
    document.querySelectorAll('.mobile-nav a').forEach(link => {
        link.addEventListener('click', function() {
            mobileNav?.classList.remove('active');
            const icon = mobileMenuBtn?.querySelector('i');
            if (icon) {
                icon.classList.add('fa-bars');
                icon.classList.remove('fa-times');
            }
        });
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            e.preventDefault();
            const target = document.querySelector(href);
            
            if (target) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                mobileNav?.classList.remove('active');
            }
        });
    });
    
    // Header scroll effect
    let lastScrollY = window.scrollY;
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;
        
        if (header) {
            if (currentScrollY > lastScrollY && currentScrollY > 100) {
                // Scrolling down
                header.style.transform = 'translateY(-100%)';
            } else {
                // Scrolling up
                header.style.transform = 'translateY(0)';
            }
            
            // Add shadow when scrolled
            if (currentScrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }
        
        lastScrollY = currentScrollY;
    });
    
    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('.card, .stat-item, .section-header').forEach(el => {
        observer.observe(el);
    });
    
    // Counter animation for statistics
    function animateCounter(element, target, duration = 2000) {
        let start = 0;
        const increment = target / (duration / 16);
        
        function updateCounter() {
            start += increment;
            if (start < target) {
                element.textContent = Math.floor(start);
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        }
        
        updateCounter();
    }
    
    // Initialize counter animations when visible
    const statObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target.querySelector('.stat-number');
                if (counter && !counter.classList.contains('animated')) {
                    const target = parseInt(counter.dataset.target || counter.textContent);
                    counter.classList.add('animated');
                    animateCounter(counter, target);
                }
            }
        });
    }, { threshold: 0.5 });
    
    document.querySelectorAll('.stat-item').forEach(item => {
        statObserver.observe(item);
    });
});

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Global mobile menu toggle function
function toggleMobileMenu(event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    
    console.log('toggleMobileMenu called', mobileNav, mobileMenuBtn); // Debug log
    
    if (mobileNav) {
        mobileNav.classList.toggle('active');
        console.log('Menu active state:', mobileNav.classList.contains('active')); // Debug log
        
        // Toggle hamburger animation
        const icon = mobileMenuBtn?.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }
    }
}

// Export for use in other scripts
window.CGMHUtils = {
    debounce
};

// Make toggleMobileMenu globally available
window.toggleMobileMenu = toggleMobileMenu;