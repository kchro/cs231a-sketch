
/**
 * task control
 */
function unlock_task_1() {
  // lock task 2
  $('#task-2-done').off('click');

  // reset task 1
  $('#task-1-done')[0].innerHTML = "done";
  $('#task-1-check').prop('checked', false);
  $('#svgContainer').on('click', 'path', function() {
    // uncheck "no strings"
    $('#task-1-check').prop('checked', false);

    // highlight functionality
    if (this.highlight === undefined) {
      this.highlight = true;
    } else {
      this.highlight = !this.highlight;
    }

    this.style.stroke = (this.highlight) ? 'red' : 'black';
  });

  // on click, "no strings" button clears all highlights
  $('#task-1-check').on('click', function() {
    if (this.checked && any_highlights()) {
      clear_highlights();
    }
  });

  // on completion, unlock task 2
  $('#task-1-done').on('click', function() {
    // check completion
    if ($('#task-1-check').is(':checked') || any_highlights()) {
      // completed task 1
      $(this).off('click');
      $('#task-1-check').off('click');
      unlock_task_2();
      this.innerHTML = "completed task";
    } else {
      print('Complete Task 1');
    }
  });
}

function unlock_task_2() {
  // lock first task
  $('#svgContainer').off('click', 'path');
  $('#svgContainer').find('path').toggleClass('disable');

  // unlock second task
  $('#startString').prop('checked', true);
  let start = null;
  let end = null;

  // reset second task
  $('#svgContainer').on('click', 'svg', function(e) {
    // calculate coordinates relative to SVG
    let offset = $(this).offset();
    const x = e.pageX - offset.left;
    const y = e.pageY - offset.top;

    if ($('#startString').is(':checked')) {
      // enforce: only one start circle
      if (start) this.removeChild(start);
      start = draw_circle(this, x, y, 'blue');
      // toggle end switch
      $('#endString').prop('checked', true);
    } else if ($('#endString').is(':checked')) {
      // enforce: only one end circle
      if (end) this.removeChild(end);
      end = draw_circle(this, x, y, 'red');
      // toggle start switch
      $('#startString').prop('checked', true);
    }
  });

  // on completion, unlock task 1
  $('#task-2-done').on('click', function() {
    // check completion
    if (!start) {
      if (!end) {
        print('Please complete Task 2');
      } else {
        print('Please mark the start of the strings');
      }
      // toggle start switch
      $('#startString').prop('checked', true);
    } else if (!end) {
      print('Please mark the end of the strings');
      // toggle start switch
      $('#endString').prop('checked', true);
    } else {
      // completed both parts of Task 2
      $('#svgContainer').off('click');
      load_next();
      unlock_task_1();
    }
  });
}

/**
 * main
 */
$(function() {
  load_next();
  unlock_task_1();
});
