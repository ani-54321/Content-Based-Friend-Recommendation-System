const buttons = document.querySelectorAll(".continue-btn");
const overlay = document.querySelector(".overlay");
const msg = document.querySelector(".overlay-message");
const main = document.querySelector(".main-section");
const htmlCourse = document.querySelector(".html-course");
const cssCourse = document.querySelector(".css-course");
const jsCourse = document.querySelector(".js-course");
const backBtns = document.querySelectorAll(".back");
const courses = document.querySelectorAll(".course-section");
const modeBtn = document.querySelector(".mode-switch");
const r = document.querySelector(":root");
const markBtns = document.querySelectorAll(".mark");
let mode = "light";

const showCourse = (course) => {
  course.style.transform = "translateX(0px)";
  course.style.display = "block";
};

const hideCourse = (course) => {
  course.style.transform = "translateX(150%)";
  course.style.display = "none";
};

modeBtn.addEventListener("click", () => {
  if (mode === "light") {
    mode = "dark";
    modeBtn.classList.remove("fa-moon");
    modeBtn.classList.add("fa-sun");
    r.style.setProperty("--mode-hover", "#ead94c");
    r.style.setProperty("--header", "#121212");
    r.style.setProperty("--bg", "#1c1c1c");
    r.style.setProperty("--text", "#ffffff");
    r.style.setProperty("--dark-grey", "rgba(255, 255, 255, 0.7)");
  } else {
    mode = "light";
    modeBtn.classList.remove("fa-sun");
    modeBtn.classList.add("fa-moon");
    r.style.setProperty("--mode-hover", "#203297");
    r.style.setProperty("--header", "#dbdbdb");
    r.style.setProperty("--bg", "#f0f0f0");
    r.style.setProperty("--text", "#050505");
    r.style.setProperty("--dark-grey", "rgba(5, 5, 5, 0.7)");
  }
});

for (let btn of buttons) {
  let courseToShow = btn.classList[1];
  switch (courseToShow) {
    case "html":
      courseToShow = htmlCourse;
      break;
    case "css":
      courseToShow = cssCourse;
      break;
    case "js":
      courseToShow = jsCourse;
      break;
  }
  btn.addEventListener("click", () => {
    overlay.style.transformOrigin = "right";
    overlay.style.transform = "scaleX(1)";
    msg.innerText = "Loading Course...";
    setTimeout(() => {
      msg.style.opacity = 1;
      hideCourse(main);
    }, 500);
    setTimeout(() => {
      msg.style.opacity = 0;
      showCourse(courseToShow);
    }, 2500);
    setTimeout(() => {
      overlay.style.transformOrigin = "left";
      overlay.style.transform = "scaleX(0)";
    }, 3000);
  });
}

for (let btn of backBtns) {
  btn.addEventListener("click", () => {
    overlay.style.transformOrigin = "right";
    overlay.style.transform = "scaleX(1)";
    msg.innerText = "Loading Courses...";
    setTimeout(() => {
      msg.style.opacity = 1;
      for (let course of courses) {
        hideCourse(course);
      }
    }, 500);
    setTimeout(() => {
      msg.style.opacity = 0;
      showCourse(main);
    }, 2500);
    setTimeout(() => {
      overlay.style.transformOrigin = "left";
      overlay.style.transform = "scaleX(0)";
    }, 3000);
  });
}

for (let btn of markBtns) {
  btn.addEventListener("click", () => {
    const parentLesson = btn.parentElement.parentElement;
    const checked = parentLesson.classList[2] ? true : false;
    if (checked) {
      parentLesson.classList.remove("checked");
      btn.innerText = "Mark as Done";
    } else {
      parentLesson.classList.add("checked");
      btn.innerText = "Mark as Incomplete";
    }
  });
}

// Some random colors
const colors = ["#3CC157", "#2AA7FF", "#1B1B1B", "#FCBC0F", "#F85F36"];

const numBalls = 50;
const balls = [];

for (let i = 0; i < numBalls; i++) {
  let ball = document.createElement("div");
  ball.classList.add("ball");
  ball.style.background = colors[Math.floor(Math.random() * colors.length)];
  ball.style.left = `${Math.floor(Math.random() * 100)}vw`;
  ball.style.top = `${Math.floor(Math.random() * 100)}vh`;
  ball.style.transform = `scale(${Math.random()})`;
  ball.style.width = `${Math.random()}em`;
  ball.style.height = ball.style.width;
  
  balls.push(ball);
  document.body.append(ball);
}

// Keyframes
balls.forEach((el, i, ra) => {
  let to = {
    x: Math.random() * (i % 2 === 0 ? -11 : 11),
    y: Math.random() * 12
  };

  let anim = el.animate(
    [
      { transform: "translate(0, 0)" },
      { transform: `translate(${to.x}rem, ${to.y}rem)` }
    ],
    {
      duration: (Math.random() + 1) * 2000, // random duration
      direction: "alternate",
      fill: "both",
      iterations: Infinity,
      easing: "ease-in-out"
    }
  );
});
