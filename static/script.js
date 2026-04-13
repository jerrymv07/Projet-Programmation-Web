document.addEventListener("DOMContentLoaded", () => {
    const items = document.querySelectorAll("li");
    items.forEach((item, index) => {
        setTimeout(() => {
            item.classList.add("fade-in");
        }, index * 100);
    });
});