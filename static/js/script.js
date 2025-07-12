// Example JavaScript code
document.addEventListener('DOMContentLoaded', function () {
    console.log('JavaScript is working!');
    const testimonials = document.querySelectorAll('.card');
    testimonials.forEach((card) => {
        card.addEventListener('mouseover', () => {
            card.style.transform = 'scale(1.05)';
            card.style.transition = 'transform 0.3s ease';
        });
        card.addEventListener('mouseout', () => {
            card.style.transform = 'scale(1)';
        });
    });
});
// Add more JavaScript functionality as needed

