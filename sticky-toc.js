const aa = document.createElement("aside")
document.body.appendChild(aa)

const headings = Array.from(document.getElementsByTagName("h2"));
const aside = document.querySelector("aside");
const ul = document.createElement("ul");
aside.appendChild(ul);
headings.map((heading) => {
    const id = heading.innerText.toLowerCase().replaceAll(" ", "_");
    heading.setAttribute("id", id);
    const anchorElement = `<a href="#${id}">${heading.textContent}</a>`;
    const keyPointer = `<li>${anchorElement}</li>`;
    ul.insertAdjacentHTML("beforeend", keyPointer);
});
const tocAnchors = aside.querySelectorAll("a");
const obFunc = (entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            const index = headings.indexOf(entry.target);
            tocAnchors.forEach((tab) => {
                tab.classList.remove("active");
            });
            tocAnchors[index].classList.add("active");
            tocAnchors[index].scrollIntoView({
                block: "nearest",
                inline: "nearest"
            });
        }
    });
};
const obOption = {
    rootMargin: "-30px 0% -77%",
    threshold: 1
};
const observer = new IntersectionObserver(obFunc, obOption);
headings.forEach((hTwo) => observer.observe(hTwo));


const style = document.createElement('style');
style.innerHTML = `
body {
    padding: 10px;
    display: grid;
    gap: 2rem;
    grid-template-columns: 3fr 1fr;
}
aside {
  padding: 16px;
  background-color: rgba(1, 1, 1, 0.2);
  align-self: start;
  position: sticky;
  top: 10px;
  border-radius: 0.2em;
  max-height: 100vh;
  overflow: auto;
}
aside ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
aside ul li {
  padding: 0.15em;
}
aside ul li a {
  color: inherit;
  text-transform: none;
  display: inline-block;
  transform-origin: left;
  transition: transform 0.1s linear;
}
aside ul li a.active {
  font-weight: 600;
  transform: scale(1.1);
}

 @media (max-width: 767px) {
    body {
      grid-template-columns: 1fr;
  }
    aside {
      display: none;
    }
  }
`;
document.body.appendChild(style)