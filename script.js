document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("a");
    links.forEach(link => {
        link.addEventListener("mouseover", () => {
            link.style.color = "#ff4500";
        });
        link.addEventListener("mouseout", () => {
            link.style.color = "#007bff";
        });
    });
});
