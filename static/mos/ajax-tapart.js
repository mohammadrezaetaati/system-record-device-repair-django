$(document).ready(function(){
    $(".btn-success").click(function(){
    var url = $(this).attr('data-url');
    const selectElement = document.querySelector("select");
    selectElement.children[0].textContent = "Select here"
        $.ajax({
            url: "{% url 'load_part_table_ajax'%}", 
            data: {'device_id':this.id},
            success: function(data){  
                $('#taPart').empty();
              var trHead = ' <thead>'+
                        '<tr class="heading">'+
                                '<th class="column-title">انتخاب</th>'+
                                '<th class="column-title">قطعه</th>'+
                                '<th class="column-title">مدل</th>'+
                                '<th class="column-title">تعداد</th>'+
                                '<tr>'+
                                '</thead>'; 
               var trHTML = '';                 
          data.forEach(function (item) {
                        trHTML +=
                                '<tr class="even pointer" >' +
                                            '<td class="a-center "><input type="checkbox" class="flat" name='+item.id+' value='+item.id+' id="pname' + item.name  + '" /></td>' +
                                            '<td>'+item.name+'</td>' +
                                            '<td>'+item.brand+'</td>' +
                                            '<td><input type="number" name='+item.id+' Style="width:50px ;" value="1"/></td>' +
                                        '</tr>';
                    });
                    console.log(trHTML);
                    $('#taPart').append(trHead);
                    $('#taPart').append(trHTML);
                }
            });
        });
    });