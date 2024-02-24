document.addEventListener('DOMContentLoaded', () => {
    fetch('./courses.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            renderJsonData(data);
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
});

document.getElementById('title').addEventListener('click', function() {
    this.classList.toggle('clicked');
});

document.getElementById('search-bar').addEventListener('click', function() {

    var testButton = document.getElementById('deleteButton');
    if (testButton) return;

    const popup_holder = document.getElementById('popup-holder');
    const popup = document.createElement('div');

    popup.style.position = "absolute";
    popup.style.top = "50%";
    popup.style.left = "50%";
    popup.style.transform = "translate(-50%, -50%)";
    popup.style.border = "1px solid black";
    popup.style.width = "450px"
    popup.style.height = "450px"
    popup.style.display = "flex";
    popup.style.justifyContent = "center";
    popup.style.alignContent = "center";
    popup.style.background = "white"
    popup.id = "popup"

    const removeButton = document.createElement('button');
    removeButton.id = "deleteButton";
    popup.appendChild(removeButton);
    popup_holder.appendChild(popup);
    removeButton.onclick = function() {deleteButton()};


});

function deleteButton() {

    var divToDelete = document.getElementById('popup');
    divToDelete.remove();
}

function renderJsonData(data) {
    const container = document.getElementById('data-container');
    container.style.display = "flex";
    container.style.flexWrap = "wrap";
    container.style.rowGap = "40px";
    container.style.justifyContent = "space-around";

    data.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('item');
        div.style.border = "1px solid black";
        div.style.padding = "25px"
        div.style.width = "450px"
        div.style.height = "150px"
        div.style.display = "flex";
        div.style.justifyContent = "space-between";

        const left = document.createElement('div');

        const code = document.createElement('h2');
        code.textContent = item.course_prefix + item.course_code;
        left.appendChild(code);

        const title = document.createElement('p');
        title.textContent = item.course_title;
        left.appendChild(title);

        const terms = document.createElement('div');
        terms.style.display = "flex";
        terms.style.flexDirection = "row";
        terms.style.gap = "40px";
        item.offered_terms.forEach(term => {
            const term_container = document.createElement('div');
            term_container.style.background = "#ccebf6";
            term_container.style.display = "flex";
            term_container.style.width = "70px";
            term_container.style.height = "50px";
            term_container.style.justifyContent = "center";
            term_container.style.alignContent = "center";
            term_container.style.borderRadius = "15px";

            const term_name = document.createElement('p');
            term_name.textContent = term;

            term_container.appendChild(term_name);
            terms.appendChild(term_container);
        });
        left.appendChild(terms);

        div.appendChild(left);


        const right = document.createElement('div');
        right.style.display = "flex";
        right.style.flexDirection = "column";
        right.style.alignItems = "flex-end"

        const rating = document.createElement('div');
        rating.style.display = "flex";
        let stars = '';
        let empty_stars = '';
        for (let i = 1; i <= 5; i++) {
            if (i <= Math.floor(item.average_stars)) {
                // Full star
                stars += '★';
            } else {
                // Empty star
                empty_stars += '★';
            }
        }
        const filledStars = document.createElement('p');
        filledStars.textContent = stars;
        filledStars.style.color = "#b78ae5";
        rating.appendChild(filledStars);

        const emptyStars = document.createElement('p');
        emptyStars.textContent = empty_stars;
        emptyStars.style.color = "#dddddd";
        rating.appendChild(emptyStars);

        right.appendChild(rating);

        const reviews = document.createElement('p');
        reviews.textContent = item.total_reviews.toString() + " reviews";
        right.appendChild(reviews);

        div.appendChild(right);


        container.appendChild(div);
    });
}

function renderStars(rating,) {
    let stars = '';
    let empty_stars = '';
    for (let i = 1; i <= 5; i++) {
        if (i <= Math.floor(rating)) {
            // Full star
            stars += '★';
        } else {
            // Empty star
            empty_stars += '★';
        }
    }
    return stars;
}

