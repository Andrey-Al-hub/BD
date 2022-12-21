var operation_button = document.querySelector("#operation_confirm_button");
operation_button.addEventListener("click", operationPrint);

var operation_select = document.getElementById("operation_selector");
function operationPrint() {
    var blocks = document.getElementsByClassName("operation");
    for (let i = 0; i < blocks.length; i += 1) {
        blocks[i].style.display = 'none';
    }
    var text = operation_select.options[operation_select.selectedIndex].text;
    if (text == "Приход товара") {
        productIncome();
    }
}

// ПРИБЫТИЕ ТОВАРА
function productIncome() {
    var operation_block = document.getElementsByClassName("operation")[0];
    var income_block = document.getElementById("income_value");
    var income_select = document.querySelector("#income_selector");
    var income_input = document.getElementsByClassName("income_input")[0];
    if (operation_block.style.display == 'none') {
        income_block.style.display = 'none';
        income_select.value = 'select';
        income_input.value = '';
    }
    operation_block.style.display = 'flex';
    income_select.addEventListener('change', productIncomeSelect)
}

function productIncomeSelect() {

    var income_select = document.querySelector("#income_selector");
    text = income_select.options[income_select.selectedIndex].text;
    var income_block = document.getElementById("income_value");
    if (text != "Выберите товар") {
//        if (text == "Добавить товар...") {
//
//        }
//        else
        income_block.style.display = 'flex';
    }
    else {
        income_block.style.display = 'none';
    }
}
