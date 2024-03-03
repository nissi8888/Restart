//Testimonial Data
const testimonials = [
    {
      name: "K Chandrakanth",
      job: "B.tech CSE",
      image: "https://icones.pro/wp-content/uploads/2021/06/symbole-du-monde-rouge.png",
      testimonial:
        "Thank You For this wonderful Course i have now completed my UG degree. It's all because of my master and my best friend Samuel thank you",
    },
    {
      name: "Mahesh",
      job: "M.tech",
      image: "https://previews.123rf.com/images/asmati/asmati1606/asmati160600182/57509137-earth-globe-sign-white-icon-on-red-background.jpg",
      testimonial:
        "First of all I want to thank Samuel for creating this wonderful website because of you I am able to complete my Master's Thank You",
    },
    {
      name: "Shiva Kumar",
      job: "MCA Computer Applications",
      image: "https://icones.pro/wp-content/uploads/2021/06/symbole-du-monde-rouge.png",
      testimonial:
        "Thank You upScale Without this course I could not complete my Masters and How can I forget my Mentor Samuel Thank You",
    },
    {
      name: "Akash",
      job: "B.com Computer Applications",
      image: "https://previews.123rf.com/images/asmati/asmati1606/asmati160600182/57509137-earth-globe-sign-white-icon-on-red-background.jpg",
      testimonial:
        "Samuel thank you for teaching me all the Subjects and making this course for me thank you very much",
    },
  ];
  
  //Current Slide
  let i = 0;
  //Total Slides
  let j = testimonials.length;
  
  let testimonialContainer = document.getElementById("testimonial-container");
  let nextBtn = document.getElementById("next");
  let prevBtn = document.getElementById("prev");
  
  nextBtn.addEventListener("click", () => {
    i = (j + i + 1) % j;
    displayTestimonial();
  });
  prevBtn.addEventListener("click", () => {
    i = (j + i - 1) % j;
    displayTestimonial();
  });
  
  let displayTestimonial = () => {
    testimonialContainer.innerHTML = `
      <p  style="font-family: 'Raleway';font-size: 18px; color: black; ">${testimonials[i].testimonial}</p>
      <br>
      <img src=${testimonials[i].image}>
      <h3>${testimonials[i].name}</h3>
      <h6>${testimonials[i].job}</h6>
    `;
  };
  window.onload = displayTestimonial;



