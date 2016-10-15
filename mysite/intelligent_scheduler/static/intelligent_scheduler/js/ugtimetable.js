$(document).ready(function() {

    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    //////////////////////////////////////////////////////////////
    var trigger = $('.hamburger'),
    overlay = $('.overlay'),
    isClosed = false;

    trigger.click(function () {
        hamburger_cross();
    });

    function hamburger_cross() {

        if (isClosed == true) {
            overlay.hide();
            trigger.removeClass('is-open');
            trigger.addClass('is-closed');
            isClosed = false;
        } else {
            overlay.show();
            trigger.removeClass('is-closed');
            trigger.addClass('is-open');
            isClosed = true;
        }
    }

    $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
    });
    ////////////////////////////////////////////////////////////////

    $('#external-events .fc-event1').each(function() {

        // store data so the calendar knows to render an event upon drop
        $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            id: $(this).attr('id'),
            duration: '01:00:00',
            stick: true // maintain when user navigates (see docs on the renderEvent method)
        });

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });

    $('#external-events .fc-event2').each(function() {

        // store data so the calendar knows to render an event upon drop
        $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            id: $(this).attr('id'),
            duration: '01:30:00',
            stick: true // maintain when user navigates (see docs on the renderEvent method)
        });

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });

    $('#external-events .fc-event3').each(function() {

        // store data so the calendar knows to render an event upon drop
        $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            id: $(this).attr('id'),
            duration: '01:30:00',
            stick: true // maintain when user navigates (see docs on the renderEvent method)
        });

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });

    $('#external-events .fc-event4').each(function() {

        // store data so the calendar knows to render an event upon drop
        $(this).data('event', {
            title: $.trim($(this).text()), // use the element's text as the event title
            id: $(this).attr('id'),
            duration: '01:30:00',
            stick: true // maintain when user navigates (see docs on the renderEvent method)
        });

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });


    $('#calendarug3').fullCalendar({
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
        defaultDate: '2016-10-10',
        droppable: true, // this allows things to be dropped onto the calendar
        selectHelper: true,
        select: function(start, end, jsEvent) {
            var title = prompt('Event Title:');
            var eventData;
            if (title) {
                eventData = {
                    title: title,
                    start: start,
                    end: end
                };
                $('#calendarug3').fullCalendar('renderEvent', eventData, true); // stick? = true
            }
            $('#calendarug3').fullCalendar('unselect');
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
            console.log('calendar 3 viewRender');
            if ($('#drop-remove3').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
        }
        //defaultView : 'agendaSixDay'
    });

    ////////////////////////////////////////////////////////////////

    $('#calendarug2').fullCalendar({
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
        defaultDate: '2016-10-10',
        droppable: true, // this allows things to be dropped onto the calendar
        selectHelper: true,
        select: function(start, end, jsEvent) {
            var title = prompt('Event Title:');
            var eventData;
            if (title) {
                eventData = {
                    title: title,
                    start: start,
                    end: end
                };
                $('#calendarug2').fullCalendar('renderEvent', eventData, true); // stick? = true
            }
            $('#calendarug2').fullCalendar('unselect');
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
            console.log('calendar 2 viewRender');
            if ($('#drop-remove2').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
        }
        //defaultView : 'agendaSixDay'
    });


    $('#calendarug1').fullCalendar({
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
        defaultDate: '2016-10-10',
        droppable: true, // this allows things to be dropped onto the calendar
        selectHelper: true,
        select: function(start, end, jsEvent) {
            var title = prompt('Event Title:');
            var eventData;
            if (title) {
                eventData = {
                    title: title,
                    start: start,
                    end: end
                };
                $('#calendarug1').fullCalendar('renderEvent', eventData, true); // stick? = true
            }
            $('#calendarug1').fullCalendar('unselect');
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
            console.log('calendar 1 viewRender');
            if ($('#drop-remove1').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }
        }
        //defaultView : 'agendaSixDay'
    });
    ///////////////////////////////////////////////////////////////////////


});
