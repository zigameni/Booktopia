var elem = document.getElementById('submit');
var form = document.getElementById('payment-form');


form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var custName = document.getElementById("custName").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;
    var postCode = document.getElementById("postCode").value;

    console.log("--------Break 0");
    // create ajax request to create order
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000/orders/add/',
        data: {
            order_key: 1,
            csrfmiddlewaretoken: CSRF_TOKEN,
            action: "post",
        },
        success: function () {
            console.log("succesfully created the order");
        }

    })

    // stripe confirm card payment
    window.location.replace("http://127.0.0.1:8000/basket/orderplaced");
});
