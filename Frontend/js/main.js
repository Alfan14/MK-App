document.getElementById('menuButton').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
        sidebar.style.display = 'block';
    } else {
        sidebar.style.display = 'none';
    }
});

// Close sidebar when clicking outside of it
document.addEventListener('click', function(event) {
    var sidebar = document.getElementById('sidebar');
    var menuButton = document.getElementById('menuButton');

    // Check if the click is outside the sidebar and menu button
    if (!sidebar.contains(event.target) && event.target !== menuButton) {
        sidebar.style.display = 'none';
    }
});

const cards = [
    { title: "Sate Kelinci", price: "Rp. 20.000", location: "Telaga Sarangan", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Bakso Pak Sutarlan", price: "Rp. 5.000", location: "Desa Pencol", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Nasi Pecel Bu Tuti", price: "Rp. 15.000", location: "Pasar Baru", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Mie Ayam Bang Ali", price: "Rp. 12.000", location: "Jalan Raya", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Tahu Campur Mamat", price: "Rp. 10.000", location: "Gang Mawar", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Es Dawet Bu Yani", price: "Rp. 8.000", location: "Jalan Cendana", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Gado-Gado Bang Udin", price: "Rp. 13.000", location: "Pasar Lama", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Soto Ayam Pak Sastro", price: "Rp. 18.000", location: "Jalan Merdeka", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Ayam Bakar Mbok Jamu", price: "Rp. 25.000", location: "Jalan Anggrek", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Sate Kelinci", price: "Rp. 20.000", location: "Telaga Sarangan", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Bakso Pak Sutarlan", price: "Rp. 5.000", location: "Desa Pencol", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Nasi Pecel Bu Tuti", price: "Rp. 15.000", location: "Pasar Baru", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Mie Ayam Bang Ali", price: "Rp. 12.000", location: "Jalan Raya", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Tahu Campur Mamat", price: "Rp. 10.000", location: "Gang Mawar", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Es Dawet Bu Yani", price: "Rp. 8.000", location: "Jalan Cendana", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Gado-Gado Bang Udin", price: "Rp. 13.000", location: "Pasar Lama", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Soto Ayam Pak Sastro", price: "Rp. 18.000", location: "Jalan Merdeka", image: "https://via.placeholder.com/150", link: "#" },
    { title: "Ayam Bakar Mbok Jamu", price: "Rp. 25.000", location: "Jalan Anggrek", image: "https://via.placeholder.com/150", link: "#" }
];

const cardsPerPage = 10;
let currentPage = 1;

function renderCards() {
    const cardContainer = document.getElementById('card-container');
    cardContainer.innerHTML = '';

    const start = (currentPage - 1) * cardsPerPage;
    const end = start + cardsPerPage;
    const paginatedCards = cards.slice(start, end);

    paginatedCards.forEach(card => {
        const cardElement = document.createElement('div');
        cardElement.className = 'card';
        cardElement.innerHTML = `
            <a href="${card.link}">
                <img src="${card.image}" alt="${card.title}">
            </a>
            <div class="title">${card.title}</div>
            <div class="price">${card.price}</div>
            <div class="location">${card.location}</div>
        `;
        cardContainer.appendChild(cardElement);
    });

    document.getElementById('pageNumber').textContent = `Page ${currentPage}`;

    document.getElementById('prevPage').disabled = currentPage === 1;
    document.getElementById('nextPage').disabled = currentPage === Math.ceil(cards.length / cardsPerPage);
}

function nextPage() {
    if (currentPage < Math.ceil(cards.length / cardsPerPage)) {
        currentPage++;
        renderCards();
    }
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        renderCards();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    renderCards();
});

function showPopup(card) {
    const popup = document.getElementById('popup');
    document.getElementById('popup-image').src = card.image;
    document.getElementById('popup-title').textContent = card.title;
    document.getElementById('popup-price').textContent = card.price;
    document.getElementById('popup-location').textContent = card.location;
    document.getElementById('popup-hours').textContent = `Buka: ${card.hours}`;
    document.getElementById('popup-map').src = card.map;
    document.getElementById('popup-route-button').href = card.link;
    popup.style.display = 'flex';

    const closeButton = document.querySelector('.close-button');
    closeButton.addEventListener('click', () => {
        popup.style.display = 'none';
    });

    window.addEventListener('click', (event) => {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
}