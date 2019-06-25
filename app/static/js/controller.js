$(document).ready(function () {
    // Activate tooltip
    $('[data-toggle="tooltip"]').tooltip();

    // Select/Deselect checkboxes
    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function () {
        if (this.checked) {
            checkbox.each(function () {
                this.checked = true;
            });
        } else {
            checkbox.each(function () {
                this.checked = false;
            });
        }
    });
    checkbox.click(function () {
        if (!this.checked) {
            $("#selectAll").prop("checked", false);
        }
    });
});


class Controller {
    constructor() {
        this.dataUser = document.getElementById("data-users");

        this.btnAddUser = document.getElementById('addUser');

        this.insertUserForm = document.getElementById('insertUserForm');

        this.modalAdd = document.getElementById('addEmployeeModal');

        this.body = document.body;

        this.dataUsers = document.getElementById('data-users');

        this.initEvents();

        this.selectUsers();
    }

    initEvents() {
        this.btnAddUser.addEventListener('click', e => {
            e.preventDefault();
            let user = this.colectData();
            if (user) {
                this.postOnBackEnd(user, id => {
                    this.insertHTML(user, id);
                });


            }
        })
            ;
    }

    selectUsers() {
        let xhr = new XMLHttpRequest();
        xhr.open("POST", 'index/search');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onloadend = (e => {
            let users = JSON.parse(xhr.responseText);
            users.forEach(user => {
                this.insertHTML(user, user.id);
            });
        });
        xhr.send();
    }


    postOnBackEnd(user, fn) {

        let xhr = new XMLHttpRequest();
        xhr.open("POST", '/index/insertUser');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onloadend = (e => {
            //this.body.className = this.body.className.replace('modal-open','');
            this.body.classList.remove('modal-open');
            this.modalAdd.classList.remove('in');
            this.body.style = '';
            this.modalAdd.style = 'display : none;';
            document.getElementsByClassName('modal-backdrop')[0].remove();
            let response = JSON.parse(xhr.responseText);
            fn(response.id);
        });
        // envia minha requisiçao ajax
        xhr.send(JSON.stringify(user));


    }

    colectData() {
        let user = {};
        let isvalid = true;
        this.btnAddUser.disable = true;
        [...this.insertUserForm].forEach(element => {
            if (element.name && element.className === 'form-control') {
                if (element.value) {
                    user[element.name] = element.value;
                } else {
                    isvalid = false;
                }
            }
        });
        if (isvalid)
            return user;
        return false;
    }



    insertHTML(data, id) {

        let html =
            `
        <td>
            <span class="custom-checkbox">
                <input type="checkbox" id="checkbox1" name="options[]" value="1">
                <label for="checkbox1"></label>
            </span>
        </td>
        <td>${data.name}</td>
        <td>${data.email}</td>
        <td>${data.address}</td>
        <td>${data.phone}</td>
        <td>
            <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons"
                    data-toggle="tooltip" title="Edit">&#xE254;</i></a>
            <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons"
                    data-toggle="tooltip" title="Delete">&#xE872;</i></a>
        </td>`

        let tr = document.createElement("tr");
        tr.innerHTML = html;
        tr.dataset.id = JSON.stringify({ id });
        this.dataUsers.appendChild(tr);
    }

}


let control = new Controller();