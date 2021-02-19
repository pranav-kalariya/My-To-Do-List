// let ulTasks = $('#ulTasks')
// let btnAdd = $('#btnAdd')
// let btnRst = $('#btnRst')
// let inpNewTask = $('#inpNewTask')
// let btnCln = $('#btnCln')
// let btnSort = $('#btnSort')

// // Add button logic
// inpNewTask.keypress((e)=> {
//     if(e.which == 13){
//         addToList()
//     }
// })

// function addToList(){
//     var listItem = $('<li>',{
//         'class': 'list-group-item'
//     })
    
//     if(inpNewTask.val() != '')
//         {
//             listItem.text(inpNewTask.val())
//         }
//     listItem.click((event) => {
//         $(event.target).toggleClass('disabled')
//     })
//     ulTasks.append(listItem)
//     // console.log(inpNewTask.val())
//     inpNewTask.val("")
//     toggleInpBtns()
// }
// function sortTasks(){
//     $('#ulTasks .disabled').appendTo(ulTasks)
//     toggleInpBtns()
// }
function toggleInpBtns(){
        btnRst.prop('disabled', inpNewTask.val() == "")
        btnAdd.prop('disabled', inpNewTask.val() == "")
        btnCln.prop('disabled', ulTasks.children().length < 1)
        btnSort.prop('disabled', ulTasks.children().length < 1)
}
// }
// inpNewTask.on('input',toggleInpBtns)
// btnAdd.click(() => {addToList()})
// btnRst.click(()=> {
//     inpNewTask.val('')
//     toggleInpBtns()
// })
// btnCln.click(() => {$('#ulTasks .disabled').remove();toggleInpBtns()})
// btnSort.click(()=> {sortTasks()})
var text_box = '<li class="card-panel" style="font-size: 20px">{message}</li>';
function getCookie(name) {
    if (!document.cookie) {
      return null;
    }
  
    const xsrfCookies = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith(name + '='));
  
    if (xsrfCookies.length === 0) {
      return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
  }



function send(username, task ) {
    $.ajax({
        url: 'tasks/',
        type: 'post',
        data: JSON.stringify({"user": username , "task": task}),
        dataType: 'json',
        success: function (data) {
            // console.info(data);
            // console.log("In send")
            // console.log(data);
            var box = text_box.replace('{message}', task);
            $('#ulTasks').append(box);
        },
        error: function (data) {console.log(data) }
    });
}


function receive() {
    $.ajax({
        url: 'tasks/',
        type: 'get',
        data: JSON.stringify({"user": username , "task": task}),
        dataType: 'json',
        success: function (data) {
            console.log(data);
            if (data.length !== 0)
            {
                for(var i=0;i<data.length;i++) {
                    console.log(data[i]);
                    box = box.replace('{message}', data[i].task);
                    $('#board').append(box);
                }
            }
        },
        error: function (data) {console.log(data) }
    });
}

function delete_task(username ,user_id){
        console.log("clean button clicked."+ user_id)
        // event.preventDefault();
        $.ajax({
            url: 'messages/delete/'+user_id+'/',
            type: 'get',
            dataType: 'json',
            success: function (data) {
                console.log(data);
            },
            error: function (data) {console.log(data) }
        });
        }