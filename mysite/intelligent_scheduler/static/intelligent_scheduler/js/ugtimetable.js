$(document).ready(function() {

  /* initialize the external events
  -----------------------------------------------------------------*/

  $('#external-events .fc-event').each(function() {

      // store data so the calendar knows to render an event upon drop
      $(this).data('event', {
          title: $.trim($(this).text()), // use the element's text as the event title
          stick: true // maintain when user navigates (see docs on the renderEvent method)
      });

      // make the event draggable using jQuery UI
      $(this).draggable({
          zIndex: 999,
          revert: true,      // will cause the event to go back to its
          revertDuration: 0  //  original position after the drag
      });

  });

  // page is now ready, initialize the calendar...

  var ug1_calendar = $('#calendar_ug1').fullCalendar({
      // put your options and callbacks here
      header: { // Display nothing at the top
          left: '',
          center: '',
          right: ''
      },
      theme: true,
      //aspectRatio: 2.44,
      //eventSources: ['events.php'],
      height: 520, // Fix height
      columnFormat: 'dddd', // Display just full length of weekday, without dates
      defaultView: 'agendaWeek', // display week view
      hiddenDays: [0,], // hide Saturday and Sunday
      weekNumbers:  false, // don't show week numbers
      minTime: '8:30:00', // display from 16 to
      maxTime: '19:00:00', // 23
      slotDuration: '00:30:00', // 15 minutes for each row
      allDaySlot: false, // don't show "all day" at the top
      selectable: true,
      editable: true,
      defaultDate: '2016-09-12',
      droppable: true, // this allows things to be dropped onto the calendar
      selectHelper: true,
      select: function(start, end) {
          var title = prompt('Event Title:');
          var eventData;
          if (title) {
              eventData = {
                  title: title,
                  start: start,
                  end: end
              };
              $('#calendar_ug1').fullCalendar('renderEvent', eventData, true); // stick? = true
          }
          $('#calendar_ug1').fullCalendar('unselect');
      },
      //select: function(start, end, allDay) {
           // Code for creating new events.
      //     alert("Create new event at " + start);
      //},
      eventResize: function( event, delta, revertFunc, jsEvent, ui, view ) {
           // Code when you resize an event (for example make it two hours longer
           alert("I just got resized!");
      },
      eventDrop: function( event, jsEvent, ui, view ) {

          // Code when you drop an element somewhere else
          alert("I'm somewhere else now");
      },
      drop: function() {
          // is the "remove after drop" checkbox checked?
          if ($('#drop-remove').is(':checked')) {
              // if so, remove the element from the "Draggable Events" list
              $(this).remove();
          }
      }
      //defaultView : 'agendaSixDay'
  })
  //$('#calendar_ug1').fullCalendar('gotoDate', '2000-01-01');

  var ug2_calendar = $('#calendar_ug2').fullCalendar({
      // put your options and callbacks here
      header: { // Display nothing at the top
          left: '',
          center: '',
          right: ''
      },
      theme: true,
      //aspectRatio: 2.44,
      //eventSources: ['events.php'],
      height: 520, // Fix height
      columnFormat: 'dddd', // Display just full length of weekday, without dates
      defaultView: 'agendaWeek', // display week view
      hiddenDays: [0,], // hide Saturday and Sunday
      weekNumbers:  false, // don't show week numbers
      minTime: '8:30:00', // display from 16 to
      maxTime: '19:00:00', // 23
      slotDuration: '00:30:00', // 15 minutes for each row
      allDaySlot: false, // don't show "all day" at the top
      selectable: true,
      editable: true,
      defaultDate: '2016-09-12',
      droppable: true, // this allows things to be dropped onto the calendar
      selectHelper: true,
      select: function(start, end) {
          var title = prompt('Event Title:');
          var eventData;
          if (title) {
              eventData = {
                  title: title,
                  start: start,
                  end: end
              };
              $('#calendar_ug2').fullCalendar('renderEvent', eventData, true); // stick? = true
          }
          $('#calendar_ug2').fullCalendar('unselect');
      },
      //select: function(start, end, allDay) {
           // Code for creating new events.
      //     alert("Create new event at " + start);
      //},
      eventResize: function( event, delta, revertFunc, jsEvent, ui, view ) {
           // Code when you resize an event (for example make it two hours longer
           alert("I just got resized!");
      },
      eventDrop: function( event, jsEvent, ui, view ) {

          // Code when you drop an element somewhere else
          alert("I'm somewhere else now");
      },
      drop: function() {
          // is the "remove after drop" checkbox checked?
          if ($('#drop-remove').is(':checked')) {
              // if so, remove the element from the "Draggable Events" list
              $(this).remove();
          }
      }
      //defaultView : 'agendaSixDay'
  })

  var ug3_calendar = $('#calendar_ug3').fullCalendar({
      // put your options and callbacks here
      header: { // Display nothing at the top
          left: '',
          center: '',
          right: ''
      },
      theme: true,
      //aspectRatio: 2.44,
      //eventSources: ['events.php'],
      height: 520, // Fix height
      columnFormat: 'dddd', // Display just full length of weekday, without dates
      defaultView: 'agendaWeek', // display week view
      hiddenDays: [0,], // hide Saturday and Sunday
      weekNumbers:  false, // don't show week numbers
      minTime: '8:30:00', // display from 16 to
      maxTime: '19:00:00', // 23
      slotDuration: '00:30:00', // 15 minutes for each row
      allDaySlot: false, // don't show "all day" at the top
      selectable: true,
      editable: true,
      defaultDate: '2016-09-12',
      droppable: true, // this allows things to be dropped onto the calendar
      selectHelper: true,
      select: function(start, end) {
          var title = prompt('Event Title:');
          var eventData;
          if (title) {
              eventData = {
                  title: title,
                  start: start,
                  end: end
              };
              $('#calendar_ug3').fullCalendar('renderEvent', eventData, true); // stick? = true
          }
          $('#calendar_ug3').fullCalendar('unselect');
      },
      //select: function(start, end, allDay) {
           // Code for creating new events.
      //     alert("Create new event at " + start);
      //},
      eventResize: function( event, delta, revertFunc, jsEvent, ui, view ) {
           // Code when you resize an event (for example make it two hours longer
           alert("I just got resized!");
      },
      eventDrop: function( event, jsEvent, ui, view ) {

          // Code when you drop an element somewhere else
          alert("I'm somewhere else now");
      },
      drop: function() {
          // is the "remove after drop" checkbox checked?
          if ($('#drop-remove').is(':checked')) {
              // if so, remove the element from the "Draggable Events" list
              $(this).remove();
          }
      }
      //defaultView : 'agendaSixDay'
  })

  var ug4_calendar = $('#calendar_ug4').fullCalendar({
      // put your options and callbacks here
      header: { // Display nothing at the top
          left: '',
          center: '',
          right: ''
      },
      theme: true,
      //aspectRatio: 2.44,
      //eventSources: ['events.php'],
      height: 520, // Fix height
      columnFormat: 'dddd', // Display just full length of weekday, without dates
      defaultView: 'agendaWeek', // display week view
      hiddenDays: [0,], // hide Saturday and Sunday
      weekNumbers:  false, // don't show week numbers
      minTime: '8:30:00', // display from 16 to
      maxTime: '19:00:00', // 23
      slotDuration: '00:30:00', // 15 minutes for each row
      allDaySlot: false, // don't show "all day" at the top
      selectable: true,
      editable: true,
      defaultDate: '2016-09-12',
      droppable: true, // this allows things to be dropped onto the calendar
      selectHelper: true,
      select: function(start, end) {
          var title = prompt('Event Title:');
          var eventData;
          if (title) {
              eventData = {
                  title: title,
                  start: start,
                  end: end
              };
              $('#calendar_ug4').fullCalendar('renderEvent', eventData, true); // stick? = true
          }
          $('#calendar_ug4').fullCalendar('unselect');
      },
      //select: function(start, end, allDay) {
           // Code for creating new events.
      //     alert("Create new event at " + start);
      //},
      eventResize: function( event, delta, revertFunc, jsEvent, ui, view ) {
           // Code when you resize an event (for example make it two hours longer
           alert("I just got resized!");
      },
      eventDrop: function( event, jsEvent, ui, view ) {

          // Code when you drop an element somewhere else
          alert("I'm somewhere else now");
      },
      drop: function() {
          // is the "remove after drop" checkbox checked?
          if ($('#drop-remove').is(':checked')) {
              // if so, remove the element from the "Draggable Events" list
              $(this).remove();
          }
      }
      //defaultView : 'agendaSixDay'
  })

});
