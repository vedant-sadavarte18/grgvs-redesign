const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));
const navLinks = `                <li><a href="goals.html">Our Goals</a></li>
                <li><a href="impact.html">Plant Data</a></li>
                <li><a href="partners.html">Partners</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="donate.html" class="btn-primary" style="color:white !important;">Donate</a></li>
            </ul>
        </div>`;

files.forEach(file => {
    if (file === 'index.html') return;
    let content = fs.readFileSync(file, 'utf8');
    
    // Fix nav links
    const badRegex = /                    <p style="color: #aaa; margin-bottom: 20px; line-height: 1\.6;">[\s\S]*?Ahmedabad, Gujarat 380051\s*<\/p>/;
    
    if (content.match(badRegex) && content.indexOf('<nav') < content.indexOf('Ahmedabad, Gujarat 380051') && content.indexOf('Ahmedabad, Gujarat 380051') < content.indexOf('</nav>')) {
        content = content.replace(badRegex, navLinks);
    }
    
    // Replace social links in footer
    const socialRegex = /<div class="social-links"[^>]*>[\s\S]*?<\/div>/g;
    
    const newAddress = `<p style="color: #aaa; margin-bottom: 20px; line-height: 1.6;">
                        <i class="fas fa-map-marker-alt" style="color: var(--secondary-color); margin-right: 10px;"></i>
                        <strong>GRGVS NGO (GUJARAT GRAM VIKAS)</strong><br>
                        BLOCK A, Siddhivinayak Business Tower, 508,<br>
                        off Sarkhej - Gandhinagar Highway, Makarba,<br>
                        Ahmedabad, Gujarat 380051
                    </p>`;
                    
    content = content.replace(socialRegex, (match, offset) => {
        // If it's the footer social links, replace it
        if (offset > content.indexOf('<footer')) {
            return newAddress;
        }
        return match;
    });

    fs.writeFileSync(file, content);
    console.log('Fixed ' + file);
});
