document.addEventListener("DOMContentLoaded", function () {
    // Select all external links
    const links = document.querySelectorAll('a[href^="http"]');
    
    links.forEach(link => {
        link.setAttribute('target', '_blank');
        link.setAttribute('rel', 'noopener noreferrer');
    });
});
