document.addEventListener("DOMContentLoaded", () => {
    let slideIndex = 0;
    const slides = document.querySelectorAll(".carousel-slide");
    const dots = document.querySelectorAll(".dot");
    const prev = document.querySelector(".prev");
    const next = document.querySelector(".next");
    let slideInterval;

    function showSlides(n) {
        // Hide all slides and remove active class from dots
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
            dots[i].classList.remove("active");
        }

        // Handle index wrapping
        if (n >= slides.length) {
            slideIndex = 0;
        } else if (n < 0) {
            slideIndex = slides.length - 1;
        } else {
            slideIndex = n;
        }

        // Show the correct slide and set dot to active
        if(slides[slideIndex]) {
            slides[slideIndex].style.display = "block";
            dots[slideIndex].classList.add("active");
        }
    }

    function plusSlides(n) {
        showSlides(slideIndex + n);
    }

    function currentSlide(n) {
        showSlides(n);
    }

    function resetInterval() {
        clearInterval(slideInterval);
        slideInterval = setInterval(() => plusSlides(1), 5000);
    }

    prev.addEventListener('click', () => {
        plusSlides(-1);
        resetInterval();
    });

    next.addEventListener('click', () => {
        plusSlides(1);
        resetInterval();
    });

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentSlide(index);
            resetInterval();
        });
    });

    // Initial setup
    showSlides(slideIndex); // Show the first slide
    resetInterval(); // Start the interval
});

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);
document.querySelectorAll('.fade-in-up').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    observer.observe(el);
});
