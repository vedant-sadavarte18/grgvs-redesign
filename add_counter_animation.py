import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find all <h3> tags inside .stat-card that have numbers
# Example: <h3 style="font-size: 2rem; color: var(--primary-color);">500,000+</h3>

def replace_stat(match):
    full_match = match.group(0)
    style = match.group(1)
    number_str = match.group(2)
    plus = match.group(3)
    
    # Extract the raw number for data-target
    raw_number = number_str.replace(',', '')
    
    return f'<h3 style="{style}" class="counter" data-target="{raw_number}">{full_match.split(">")[1]}'

new_content = re.sub(
    r'<h3 style="([^"]+);">([\d,]+)(\+?)</h3>',
    replace_stat,
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
# 2. Update script.js with counter animation logic
with open('script.js', 'r', encoding='utf-8') as f:
    script_content = f.read()

if 'counter' not in script_content:
    counter_code = """
// Counter Animation
const counters = document.querySelectorAll('.counter');
const speed = 200; // The lower the slower

const animateCounters = () => {
    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            // get current text without commas or +
            let rawCurrent = counter.innerText.replace(/,/g, '').replace('+', '');
            const count = +rawCurrent || 0;

            const inc = target / speed;

            if (count < target) {
                let current = Math.ceil(count + inc);
                // format with commas if target > 999
                let displayStr = current.toLocaleString();
                if (counter.innerText.includes('+') || target >= 50) { // simple heuristic to keep the plus
                    displayStr += '+';
                }
                counter.innerText = displayStr;
                setTimeout(updateCount, 15);
            } else {
                let displayStr = target.toLocaleString();
                if (counter.innerText.includes('+') || target >= 50) {
                    displayStr += '+';
                }
                counter.innerText = displayStr;
            }
        };
        
        // Start from 0 initially so animation works correctly
        counter.innerText = '0+';
        updateCount();
    });
};

// Use IntersectionObserver to start animation when visible
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounters();
            // Optional: disconnect after animating once
            observer.disconnect();
        }
    });
}, observerOptions);

// Observe the section containing the counters
const statsSection = document.querySelector('.stats-grid');
if (statsSection && counters.length > 0) {
    observer.observe(statsSection);
}
"""
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write('\n\n' + counter_code)

print("Added counter animation to index.html and script.js")
