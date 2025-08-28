document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Xóa class 'active' khỏi tất cả các link
            navLinks.forEach(nav => nav.classList.remove('active'));

            // Thêm class 'active' vào link được nhấn
            link.classList.add('active');
        });
    });
});