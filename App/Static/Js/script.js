// Client-side validation or UI enhancements
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    
    if (form) {
        form.addEventListener('submit', (e) => {
            const name = document.getElementById('name').value;
            const room = document.getElementById('room').value;
            const issue = document.getElementById('issue').value;

            if (!name || !room || !issue) {
                alert('Please fill in all fields before submitting.');
                e.preventDefault();
            } else {
                console.log('Form submitted for:', name);
            }
        });
    }

    // Auto-hide flash messages after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});