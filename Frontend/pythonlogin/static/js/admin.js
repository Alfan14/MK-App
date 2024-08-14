// add hovered class to selected list item
let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggle = document.querySelector(".toggle");
let navigation = document.querySelector(".navigation");
let main = document.querySelector(".main");

toggle.onclick = function () {
  navigation.classList.toggle("active");
  main.classList.toggle("active");
};
//Live customers
function fetchLiveUsers() {
    fetch('/pythonlogin/live_users')
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Add this line to inspect the response
            let userTable = document.getElementById('recentCustomers');
            userTable.innerHTML = ''; // Clear existing table rows

            if (Array.isArray(data)) {
                data.forEach(client => {
                    let imagePath = client.image.replace('static/', '');
                    let row = `
                        <tr>
                            <td width="60px"><div class="imgBx"><img src="/static/${imagePath}" alt="User Image" width="50" height="50"></div></td>
                            <td>${client.username}</td>
                            <td>${client.email}</td>
                        </tr>
                    `;
                    userTable.innerHTML += row;
                });
            } else {
                console.error('Expected an array but received:', data);
            }
        })
        .catch(error => console.error('Error fetching live users:', error));
}

// Refresh the user list every 5 seconds
setInterval(fetchLiveUsers, 5000);

// Call it immediately once to load the data on page load
fetchLiveUsers();
