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

console.log('oi');

class Controller {
    constructor() {
        this.dataUser = document.getElementById("#data-users");
    }




    insertHTML(contentTr,data) {
        let html =
            `<tr>
        <td>
            <span class="custom-checkbox">
                <input type="checkbox" id="checkbox1" name="options[]" value="1">
                <label for="checkbox1"></label>
            </span>
        </td>
        <td>Thomas Hardy</td>
        <td>${data.email}</td>
        <td>${data.address}</td>
        <td>${data.phone}</td>
        <td>
            <a href="#editEmployeeModal" class="edit" data-toggle="modal"><i class="material-icons"
                    data-toggle="tooltip" title="Edit">&#xE254;</i></a>
            <a href="#deleteEmployeeModal" class="delete" data-toggle="modal"><i class="material-icons"
                    data-toggle="tooltip" title="Delete">&#xE872;</i></a>
        </td>
    </tr>`
    }

    addEvents(tr){

    }
}


let contr = new Controller();