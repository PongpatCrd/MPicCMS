String.prototype.format = String.prototype.f = function() {
  var s = this,
      i = arguments.length;

  while (i--) {
      s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
  }
  return s;
};

function loading_screen(is_turn_on){
  if(is_turn_on){
    $(".loading-warpper").show();
  }
  else{
    $(".loading-warpper").hide();
  }
}

// make input type text to datepicker
function make_input_to_datepicker(element_id){
  $(element_id).datepicker({
    dateFormat: 'ddmmyy'
  });
  $(element_id).attr( 'readOnly' , 'true' );
}

// make input type text to datepicker
function make_input_to_datepicker_disabled_past(element_id){
  $(element_id).datepicker({
    dateFormat: 'ddmmyy',
    minDate: -7
  });
  $(element_id).attr( 'readOnly' , 'true' );
}

function check_is_active_icon(element_id, check_status){
  if(check_status){
    $(element_id).attr('class', 'fas fa-check-square');
  }
  else{
    $(element_id).attr('class', 'fas fa-square');
  }
}

function get_timestamp(){
  let current_date = new Date();
  let date = current_date.getDate();
  let month = current_date.getMonth()+1;
  let year = current_date.getFullYear();
  let hours = current_date.getHours();
  let minutes = current_date.getMinutes();
  let sec = current_date.getSeconds();
  let mili = current_date.getUTCMilliseconds();

  if(date < 10){
    date = "0" + date.toString();
  }

  if(month < 10){
    month = "0" + month.toString();
  }

  if(hours < 10){
    hours = "0" + hours.toString();
  }

  if(minutes < 10){
    minutes = "0" + minutes.toString();
  }

  if(sec < 10){
    sec = "0" + sec.toString();
  }

  let time_stamp = year + "-" + month + "-" + date + " " + hours + ":" + minutes + ":" + sec + "." + mili;
  return time_stamp;
}

function get_datetime(){
  let current_date = new Date();
  let date = current_date.getDate();
  let month = current_date.getMonth()+1;
  let year = current_date.getFullYear();
  let hours = current_date.getHours();
  let minutes = current_date.getMinutes();
  let sec = current_date.getSeconds();

  let month_names = [
    'มกราคม', 
    'กุมภาพันธ์',
    'มีนาคม',
    'เมษายน',
    'พฤษภาคม',
    'มิถุนายน',
    'กรกฎาคม',
    'สิงหาคม',
    'กันยายน',
    'ตุลาคม',
    'พฤศจิกายน',
    'ธันวาคม'
  ]

  if(date < 10){
    date = "0" + date.toString();
  }

  month = month_names[month];

  year = year + 543;

  if(hours < 10){
    hours = "0" + hours.toString();
  }

  if(minutes < 10){
    minutes = "0" + minutes.toString();
  }

  if(sec < 10){
    sec = "0" + sec.toString();
  }

  let time_stamp = date + " " + month + " " + year + " เวลา " + hours + ":" + minutes + ":" + sec;
  return time_stamp;
}

function createUUID() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
  var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
  return v.toString(16);
  });
}

function show_all_textarea(element){
  var scroll_height = $(element).get(0).scrollHeight;
	$(element).css('height', scroll_height + 'px');
}