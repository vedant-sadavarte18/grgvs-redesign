// Navbar scroll effect
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 10) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile menu toggle
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');

if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        navLinks.classList.remove('active');
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Counter animation
const counters = document.querySelectorAll('.counter');
const speed = 200; // The lower the slower

const animateCounters = () => {
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const currentStr = counter.innerText.replace(/,/g, '').replace('+', '');
            const count = +currentStr || 0;
            
            const inc = target / speed;

            if (count < target) {
                let current = Math.ceil(count + inc);
                counter.innerText = current.toLocaleString() + '+';
                setTimeout(updateCount, 20);
            } else {
                counter.innerText = target.toLocaleString() + '+';
            }
        };
        // Reset to 0 before starting if it's currently at target
        if (!counter.hasAttribute('data-animating')) {
            counter.setAttribute('data-animating', 'true');
            counter.innerText = '0+';
            updateCount();
        }
    });
};

// Scroll reveal using Intersection Observer
const revealElements = document.querySelectorAll('.project-card, .cred-item, .about-text');

revealElements.forEach(el => el.classList.add('reveal'));

const revealOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
};

const revealOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        } else {
            entry.target.classList.add('active');
            observer.unobserve(entry.target);
        }
    });
}, revealOptions);

revealElements.forEach(el => {
    revealOnScroll.observe(el);
});

// Start counter animation when stats section is in view
const statsSections = document.querySelectorAll('.stats, .stats-grid');

const statsObserver = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            observer.unobserve(entry.target);
        }
    });
}, revealOptions);

if(statsSections.length > 0) {
    statsSections.forEach(sec => statsObserver.observe(sec));
}


