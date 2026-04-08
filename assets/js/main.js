// Main JavaScript - CGMH Burn Center v2

document.addEventListener('DOMContentLoaded', function() {
    initializeMobileMenu();
    initializeSubmenuToggles();
    initializeClickOutsideClose();
    initializeMobileNavLinks();
    initializeSmoothScrolling();
    initializeScrollEffect();
    initializeAnimations();
    initializeCounterAnimations();
});

// Mobile Menu
function initializeMobileMenu() {
    var mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    var mobileNav = document.querySelector('.mobile-nav');

    if (!mobileMenuBtn || !mobileNav) return;

    mobileMenuBtn.addEventListener('click', function(e) {
        e.preventDefault();
        e.stopPropagation();

        mobileNav.classList.toggle('active');

        var icon = this.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }
    });
}

// Submenu toggle
function initializeSubmenuToggles() {
    var submenuToggles = document.querySelectorAll('.mobile-submenu-toggle');

    submenuToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            var menuItem = this.closest('.mobile-menu-item');
            var submenu = menuItem.querySelector('.mobile-submenu');
            if (!submenu) return;

            var isActive = submenu.classList.contains('active');

            // Close all other submenus
            document.querySelectorAll('.mobile-submenu.active').forEach(function(other) {
                if (other !== submenu) {
                    other.classList.remove('active');
                    var otherToggle = other.closest('.mobile-menu-item').querySelector('.mobile-submenu-toggle');
                    if (otherToggle) otherToggle.classList.remove('active');
                }
            });

            // Toggle current
            submenu.classList.toggle('active', !isActive);
            this.classList.toggle('active', !isActive);
        });
    });
}

// Close mobile menu on outside click
function initializeClickOutsideClose() {
    var mobileNav = document.querySelector('.mobile-nav');
    var mobileMenuBtn = document.querySelector('.mobile-menu-btn');

    document.addEventListener('click', function(e) {
        if (mobileNav && !e.target.closest('.header') && !e.target.closest('.mobile-nav')) {
            closeMobileMenu(mobileNav, mobileMenuBtn);
        }
    });
}

// Close mobile menu on link click
function initializeMobileNavLinks() {
    var mobileNav = document.querySelector('.mobile-nav');
    var mobileMenuBtn = document.querySelector('.mobile-menu-btn');

    document.querySelectorAll('.mobile-nav a').forEach(function(link) {
        link.addEventListener('click', function() {
            closeMobileMenu(mobileNav, mobileMenuBtn);
        });
    });
}

function closeMobileMenu(mobileNav, mobileMenuBtn) {
    if (!mobileNav) return;
    mobileNav.classList.remove('active');
    var icon = mobileMenuBtn && mobileMenuBtn.querySelector('i');
    if (icon) {
        icon.classList.add('fa-bars');
        icon.classList.remove('fa-times');
    }
}

// Smooth scrolling for anchor links
function initializeSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            var target = document.querySelector(href);

            if (target) {
                var header = document.querySelector('.header');
                var headerHeight = header ? header.offsetHeight : 0;
                var targetPosition = target.offsetTop - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                var mobileNav = document.querySelector('.mobile-nav');
                if (mobileNav) mobileNav.classList.remove('active');
            }
        });
    });
}

// Header hide-on-scroll and shadow
function initializeScrollEffect() {
    var lastScrollY = window.scrollY;
    var header = document.querySelector('.header');
    if (!header) return;

    window.addEventListener('scroll', function() {
        var currentScrollY = window.scrollY;

        if (currentScrollY > lastScrollY && currentScrollY > 100) {
            header.style.transform = 'translateY(-100%)';
        } else {
            header.style.transform = 'translateY(0)';
        }

        if (currentScrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        lastScrollY = currentScrollY;
    });
}

// Intersection Observer for fade-in animations
function initializeAnimations() {
    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    document.querySelectorAll('.card, .stat-item, .section-header').forEach(function(el) {
        observer.observe(el);
    });
}

// Counter animation for statistics
function initializeCounterAnimations() {
    var statObserver = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                var counter = entry.target.querySelector('.stat-number');
                if (counter && !counter.classList.contains('animated')) {
                    var target = parseInt(counter.dataset.target || counter.textContent);
                    counter.classList.add('animated');
                    animateCounter(counter, target);
                }
            }
        });
    }, { threshold: 0.5 });

    document.querySelectorAll('.stat-item').forEach(function(item) {
        statObserver.observe(item);
    });
}

function animateCounter(element, target, duration) {
    duration = duration || 2000;
    var start = 0;
    var increment = target / (duration / 16);

    function update() {
        start += increment;
        if (start < target) {
            element.textContent = Math.floor(start);
            requestAnimationFrame(update);
        } else {
            element.textContent = target;
        }
    }

    update();
}
