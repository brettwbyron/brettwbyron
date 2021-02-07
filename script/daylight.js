$( document ).ready( function () {
    //*************************************
    //****** Daylight Visualization *******
    //*************************************

    // Main daylight visualization variables
    // var w = 1200;
    // var h = 700;
    var padding = 40;
    var w = 1000;
    var h = 525;
    var hSun = 200;


    // Range of every hour in the year
    var hourRange = d3.time.hours( new Date( 2013, 0, 1, 0 ), new Date( 2013, 11, 31 ) );

    // Sunlight Data for each hour in the year 2013
    // Indexing: (0)[Hour], (1)[Day], (2)[Month], (3)[Year], (4)[Solar Azimuth Angle],
    //   (5)[Solar Elevation Angle], (6)[Equation of Time], (7)[Solar Declination Angle],
    //   (8)[Cosine of Solar Zenith Angle]
    var dataRaw = new Array()
    for ( var i = 0; i < hourRange.length; i++ ) {
        dataRaw[ i ] = calcSun( new currentHour( hourRange[ i ] ), new place( 39, 9, 55, 86, 31, 25, 5, 0 ) );
    }

    // Max/min sun values
    var minSun = d3.min( dataRaw, function ( d ) {
        return +d[ 5 ];
    } );
    var maxSun = d3.max( dataRaw, function ( d ) {
        return +d[ 5 ];
    } );



    // x-axis labels (each month)
    var monthNames = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ];


    // y-scale (sun): duration of time (days)
    var ySun = d3.time.scale()
        .domain( [ new Date( 2013, 0, 1 ), new Date( 2013, 0, 1, 23, 59 ) ] )
        .range( [ 8, hSun ] );

    // x-scale: duration of time (hours)
    var xSun = d3.time.scale()
        .domain( [ new Date( 2013, 0, 1 ), new Date( 2013, 11, 31 ) ] )
        .range( [ 1.5, w ] );

    // Noon label
    function yAxisLabel( d ) {
        if ( d == 12 ) {
            return "NOON";
        }
    }

    // Mid-Month Labels
    function midMonthDates() {
        return d3.range( 0, 12 ).map( function ( i ) {
            return new Date( 2013, i, 15 );
        } );
    }

    // Color fill selection
    function getColor( color ) {
        var colorRange = d3.scale.linear()
            .domain( [ minSun, minSun / 4, 0, maxSun / 4, maxSun ] )
            .range( [ '#011933', '#31355f', '#e2a3c3', '#eac1c8', '#fcffd9' ] );
        return colorRange( color | 0 );
    }

    // Daylight viz svg
    var sunViz = d3.select( '.data-viz' )
        .append( 'svg' )
        .attr( 'width', w + padding * 2 )
        .attr( 'height', hSun + padding * 2 );

    var axisGroup = sunViz.append( 'g' )
        .attr( 'transform', 'translate(' + padding + ', ' + padding + ')' );


    axisGroup.selectAll( '.xTicks' )
        .data( midMonthDates )
        .enter()
        .append( 'line' )
        .attr( 'x1', xSun )
        .attr( 'y1', -5 )
        .attr( 'x2', xSun )
        .attr( 'y2', hSun )
        .attr( 'stroke', 'gray' )
        .attr( 'class', 'xTicks' );

    axisGroup.selectAll( 'text.xAxisTop' )
        .data( midMonthDates )
        .enter()
        .append( 'text' )
        .text( function ( d, i ) {
            return monthNames[ i ];
        } )
        .attr( 'x', xSun )
        .attr( 'y', -8 )
        .attr( 'text-anchor', 'middle' )
        .attr( 'class', 'axis xAxisTop' );

    axisGroup.selectAll( '.yTicks' )
        .data( d3.range( 5, 22 ) )
        .enter()
        .append( 'line' )
        .attr( 'x1', -5 )
        .attr( 'y1', hSun / 2 )
        .attr( 'x2', w )
        .attr( 'y2', hSun / 2 )
        .attr( 'stroke', 'gray' )
        .attr( 'class', 'yTicks' );

    axisGroup.selectAll( 'text.yAxisLeft' )
        .data( d3.range( 5, 22 ) )
        .enter()
        .append( 'text' )
        .text( yAxisLabel )
        .attr( 'x', -7 )
        .attr( 'y', function ( d ) {
            return ySun( new Date( 2013, 0, 1, d ) ) - 4;
        } )
        .attr( 'dy', '3' )
        .attr( 'class', 'yAxisLeft' )
        .attr( 'text-anchor', 'end' );


    var lineGroup = sunViz.append( 'g' )
        .attr( 'transform', 'translate(' + padding + ', ' + padding + ')' );

    lineGroup.append( 'rect' )
        .attr( 'x', 0 )
        .attr( 'y', 0 )
        .attr( 'height', hSun )
        .attr( 'width', w )
        .attr( 'fill', '#3f3f3f' );

    lineGroup.append( 'line' )
        .attr( 'x1', 0 )
        .attr( 'y1', d3.round( ySun( new Date( 2013, 0, 1, 12 ) ) ) + 0.5 )
        .attr( 'x2', w )
        .attr( 'y2', d3.round( ySun( new Date( 2013, 0, 1, 12 ) ) ) + 0.5 )
        .attr( 'stroke', 'gray' );

    lineGroup.selectAll( 'ellipse' )
        .data( dataRaw )
        .enter()
        .append( 'ellipse' )
        .attr( 'cx', function ( d ) {
            return xSun( new Date( 2013, d[ 2 ], d[ 1 ] ) );
        } )
        .attr( 'cy', function ( d ) {
            return ySun( new Date( 2013, 0, 1, d[ 0 ] ) );
        } )
        .attr( 'rx', 1 )
        .attr( 'ry', 3.5 )
        .style( 'fill', function ( d ) {
            return getColor( d[ 5 ] );
        } );

    //*************************************
    //*************************************
    //**** Main Daylight Calculations *****
    //*************************************
    //*************************************

    //*********** End results *************
    //-Equation of Time(EOT)
    //	The difference of the speed of the sun depending on the time of year.
    //-Solar Declination Angle
    //	The declination of the sun. Angle ranges from -23.44 to + 23.44 degrees.
    //		Differs dependant on the latitude of location. 0 degrees = the Equator.
    //-Solar Azimuth Angle
    //	Angle measured clockwise from true north to the point on the horizon
    //		directly below the object (Sun).
    //-Solar Elevation Angle
    //	Angle measured vertically from the point on the horizon directly below the
    //		object (Sun) up to the object (Sun).
    //-Cosine of Zenith Angle
    //	Used to calculate the vertical component of direct sunlight shining on a
    //		horizontal surface.
    //*************************************

    //*************************************



    //************ Structures *************

    function place( latDeg, latMin, latSec, lonDeg, lonMin, lonSec, zoneHr, dst ) {
        this.latDeg = latDeg;
        // this.latMin = latMin;
        this.latMin = 0;
        // this.latSec = latSec;
        this.latSec = 0;
        this.lonDeg = lonDeg;
        // this.lonMin = lonMin;
        this.lonMin = 0;
        // this.lonSec = lonSec;
        this.lonSec = 0;
        this.zoneHr = zoneHr;
        this.dst = dst;
    }

    function currentHour( instance ) {
        this.hour = parseFloat( instance.getHours() );
        this.day = parseFloat( instance.getDate() );
        this.month = parseFloat( instance.getMonth() ) + 1;
        this.year = parseFloat( instance.getFullYear() );
        this.azimuth = 0.0;
        this.elevation = 0.0;
        this.eqTime = 0.0;
        this.solarDec = 0.0;
        this.coszen = 0.0;
    }

    //*************************************


    //*********** Subroutines *************

    // Convert radian angle to degrees
    function radToDeg( angleRad ) {
        return ( 180.0 * angleRad / Math.PI );
    }

    // Convert degree angle to radians
    function degToRad( angleDeg ) {
        return ( Math.PI * angleDeg / 180.0 );
    }

    //*************************************


    //********** Calculations *************

    // // Sets latitude and longitude depending on DST
    // function setLatLong( f ) {
    //     f[ 'latDeg' ].value = thePlace.lat;
    //     f[ 'lonDeg' ].value = thePlace.lng;
    //     f[ 'latMin' ].value = 0;
    //     f[ 'latSec' ].value = 0;
    //     f[ 'lonMin' ].value = 0;
    //     f[ 'lonSec' ].value = 0;

    //     convLatLong( f )

    //     f[ 'hrsToGMT' ].value = thePlace.utcOffset;
    // }

    // 'isLeapYear' returns 1 if the yr is a leap year, 0 if its not
    function isLeapYear( yr ) {
        return ( ( yr % 4 == 0 && yr % 100 != 0 ) || yr % 400 == 0 );
    }

    // 'convLatLong' converts any type of lat/long into the correct form
    //	 It is nested in the 'calcSun' function.
    function convLatLong( f ) {
        if ( f[ "latDeg" ].value == "" ) {
            f[ "latDeg" ].value = 0;
        }
        if ( f[ "latMin" ].value == "" ) {
            f[ "latMin" ].value = 0;
        }
        if ( f[ "latSec" ].value == "" ) {
            f[ "latSec" ].value = 0;
        }
        if ( f[ "lonDeg" ].value == "" ) {
            f[ "lonDeg" ].value = 0;
        }
        if ( f[ "lonMin" ].value == "" ) {
            f[ "lonMin" ].value = 0;
        }
        if ( f[ "lonSec" ].value == "" ) {
            f[ "lonSec" ].value = 0;
        }

        var neg = 0;
        if ( f[ "latDeg" ].value.charAt( 0 ) == '-' ) {
            neg = 1;
        }

        if ( neg != 1 ) {
            var latSeconds = ( parseFloat( f[ "latDeg" ].value ) ) * 3600 + parseFloat( f[ "latMin" ].value ) * 60 + parseFloat( f[ "latSec" ].value ) * 1;

            f[ "latDeg" ].value = Math.floor( latSeconds / 3600 );
            f[ "latMin" ].value = Math.floor( ( latSeconds - ( parseFloat( f[ "latDeg" ].value ) * 3600 ) ) / 60 );
            f[ "latSec" ].value = Math.floor( ( latSeconds - ( parseFloat( f[ "latDeg" ].value ) * 3600 ) - ( parseFloat( f[ "latMin" ].value ) * 60 ) ) + 0.5 );

        } else if ( parseFloat( f[ "latDeg" ].value ) > -1 ) {
            var latSeconds = parseFloat( f[ "latDeg" ].value ) * 3600 - parseFloat( f[ "latMin" ].value ) * 60 - parseFloat( f[ "latSec" ].value ) * 1;

            f[ "latDeg" ].value = "-0";
            f[ "latMin" ].value = Math.floor( ( -latSeconds ) / 60 );
            f[ "latSec" ].value = Math.floor( ( -latSeconds - ( parseFloat( f[ "latMin" ].value ) * 60 ) ) + 0.5 );

        } else {
            var latSeconds = parseFloat( f[ "latDeg" ].value ) * 3600 - parseFloat( f[ "latMin" ].value ) * 60 - parseFloat( f[ "latSec" ].value ) * 1;

            f[ "latDeg" ].value = Math.ceil( latSeconds / 3600 );
            f[ "latMin" ].value = Math.floor( ( -latSeconds + ( parseFloat( f[ "latDeg" ].value ) * 3600 ) ) / 60 );
            f[ "latSec" ].value = Math.floor( ( -latSeconds + ( parseFloat( f[ "latDeg" ].value ) * 3600 ) - ( parseFloat( f[ "latMin" ].value ) * 60 ) ) + 0.5 );
        }


        neg = 0;
        if ( f[ "lonDeg" ].value.charAt( 0 ) == '-' ) {
            neg = 1;
        }

        if ( neg != 1 ) {
            var lonSeconds = parseFloat( f[ "lonDeg" ].value ) * 3600 + parseFloat( f[ "lonMin" ].value ) * 60 + parseFloat( f[ "lonSec" ].value ) * 1;
            f[ "lonDeg" ].value = Math.floor( lonSeconds / 3600 );
            f[ "lonMin" ].value = Math.floor( ( lonSeconds - ( parseFloat( f[ "lonDeg" ].value ) * 3600 ) ) / 60 );
            f[ "lonSec" ].value = Math.floor( ( lonSeconds - ( parseFloat( f[ "lonDeg" ].value ) * 3600 ) - ( parseFloat( f[ "lonMin" ].value ) ) * 60 ) + 0.5 );
        } else if ( parseFloat( f[ "lonDeg" ].value ) > -1 ) {
            var lonSeconds = parseFloat( f[ "lonDeg" ].value ) * 3600 - parseFloat( f[ "lonMin" ].value ) * 60 - parseFloat( f[ "lonSec" ].value ) * 1;

            f[ "lonDeg" ].value = "-0";
            f[ "lonMin" ].value = Math.floor( ( -lonSeconds ) / 60 );
            f[ "lonSec" ].value = Math.floor( ( -lonSeconds - ( parseFloat( f[ "lonMin" ].value ) * 60 ) ) + 0.5 );

        } else {
            var lonSeconds = parseFloat( f[ "lonDeg" ].value ) * 3600 - parseFloat( f[ "lonMin" ].value ) * 60 - parseFloat( f[ "lonSec" ].value ) * 1;
            f[ "lonDeg" ].value = Math.ceil( lonSeconds / 3600 );
            f[ "lonMin" ].value = Math.floor( ( -lonSeconds + ( parseFloat( f[ "lonDeg" ].value ) * 3600 ) ) / 60 );
            f[ "lonSec" ].value = Math.floor( ( -lonSeconds + ( parseFloat( f[ "lonDeg" ].value ) * 3600 ) - ( parseFloat( f[ "lonMin" ].value ) * 60 ) ) + 0.5 );
        }
    }

    // Returns the numerical day of year
    function calcDayOfYear( month, day, lpyr ) {
        var k = ( lpyr ? 1 : 2 );
        var doy = Math.floor( ( 275 * month ) / 9 ) - k * Math.floor( ( month + 9 ) / 12 ) + day - 30;
        return doy;
    }

    // Returns Julian day corresponding to the date
    function calcJD( year, month, day ) {
        if ( month <= 2 ) {
            year -= 1;
            month += 12;
        }
        var A = Math.floor( year / 100 );
        var B = 2 - A + Math.floor( A / 4 );

        var JD = Math.floor( 365.25 * ( year + 4716 ) ) + Math.floor( 30.6001 * ( month + 1 ) ) + day + B - 1524.5;
        return JD;
    }

    // Convert Julian Day to centuries since J2000.0
    function calcTimeJulianCent( jd ) {
        var T = ( jd - 2451545.0 ) / 36525.0;
        return T;
    }

    // Convert centuries since J2000.0 to Julian Day
    function calcJDFromJulianCent( t ) {
        var JD = t * 36525.0 + 2451545.0;
        return JD;
    }

    // Calculate the Geometric Mean Longitude of the Sun.
    function calcGeomMeanLongSun( t ) {
        var L0 = 280.46646 + t * ( 36000.76983 + 0.0003032 * t );
        while ( L0 > 360.0 ) {
            L0 -= 360.0;
        }
        while ( L0 < 0.0 ) {
            L0 += 360.0;
        }
        return L0; // in degrees
    }

    // Calculate the Geometric Mean Anomaly of the Sun
    function calcGeomMeanAnomalySun( t ) {
        var M = 357.52911 + t * ( 35999.05029 - 0.0001537 * t );
        return M; // in degrees
    }

    // Calculate the eccentricity of earth's orbit
    function calcEccentricityEarthOrbit( t ) {
        var e = 0.016708634 - t * ( 0.000042037 + 0.0000001267 * t );
        return e; // unitless
    }

    // Calculate the equation of center for the sun
    function calcSunEqOfCenter( t ) {
        var m = calcGeomMeanAnomalySun( t );

        var mrad = degToRad( m );
        var sinm = Math.sin( mrad );
        var sin2m = Math.sin( mrad + mrad );
        var sin3m = Math.sin( mrad + mrad + mrad );

        var C = sinm * ( 1.914602 - t * ( 0.004817 + 0.000014 * t ) ) + sin2m * ( 0.019993 - 0.000101 * t ) + sin3m * 0.000289;
        return C; // in degrees
    }

    // Calculate the true longitude of the sun
    function calcSunTrueLong( t ) {
        var l0 = calcGeomMeanLongSun( t );
        var c = calcSunEqOfCenter( t );

        var O = l0 + c;
        return O; // in degrees
    }

    // Calculate the true anamoly of the sun
    function calcSunTrueAnomaly( t ) {
        var m = calcGeomMeanAnomalySun( t );
        var c = calcSunEqOfCenter( t );

        var v = m + c;
        return v; // in degrees
    }

    // Calculate the distance to the sun in AU
    function calcSunRadVector( t ) {
        var v = calcSunTrueAnomaly( t );
        var e = calcEccentricityEarthOrbit( t );

        var R = ( 1.000001018 * ( 1 - e * e ) ) / ( 1 + e * Math.cos( degToRad( v ) ) );
        return R; // in AUs
    }

    // Calculate the apparent longitude of the sun
    function calcSunApparentLong( t ) {
        var o = calcSunTrueLong( t );

        var omega = 125.04 - 1934.136 * t;
        var lambda = o - 0.00569 - 0.00478 * Math.sin( degToRad( omega ) );
        return lambda; // in degrees
    }

    // Calculate the mean obliquity of the ecliptic
    function calcMeanObliquityOfEcliptic( t ) {
        var seconds = 21.448 - t * ( 46.8150 + t * ( 0.00059 - t * ( 0.001813 ) ) );
        var e0 = 23.0 + ( 26.0 + ( seconds / 60.0 ) ) / 60.0;
        return e0; // in degrees
    }

    // Calculate the corrected obliquity of the ecliptic
    function calcObliquityCorrection( t ) {
        var e0 = calcMeanObliquityOfEcliptic( t );

        var omega = 125.04 - 1934.136 * t;
        var e = e0 + 0.00256 * Math.cos( degToRad( omega ) );
        return e; // in degrees
    }

    // Calculate the right ascension of the sun
    function calcSunRtAscension( t ) {
        var e = calcObliquityCorrection( t );
        var lambda = calcSunApparentLong( t );

        var tananum = ( Math.cos( degToRad( e ) ) * Math.sin( degToRad( lambda ) ) );
        var tanadenom = ( Math.cos( degToRad( lambda ) ) );
        var alpha = radToDeg( Math.atan2( tananum, tanadenom ) );
        return alpha; // in degrees
    }

    // Calculate the declination angle of the sun
    function calcSunDeclination( t ) {
        var e = calcObliquityCorrection( t );
        var lambda = calcSunApparentLong( t );

        var sint = Math.sin( degToRad( e ) ) * Math.sin( degToRad( lambda ) );
        var theta = radToDeg( Math.asin( sint ) );
        return theta; // in degrees
    }

    // Calculate E.O.T. (the difference between true solar time and mean solar time)
    function calcEquationOfTime( t ) {
        var epsilon = calcObliquityCorrection( t );
        var l0 = calcGeomMeanLongSun( t );
        var e = calcEccentricityEarthOrbit( t );
        var m = calcGeomMeanAnomalySun( t );

        var y = Math.tan( degToRad( epsilon ) / 2.0 );
        y *= y;

        var sin2l0 = Math.sin( 2.0 * degToRad( l0 ) );
        var sinm = Math.sin( degToRad( m ) );
        var cos2l0 = Math.cos( 2.0 * degToRad( l0 ) );
        var sin4l0 = Math.sin( 4.0 * degToRad( l0 ) );
        var sin2m = Math.sin( 2.0 * degToRad( m ) );

        var Etime = y * sin2l0 - 2.0 * e * sinm + 4.0 * e * y * sinm * cos2l0 -
            0.5 * y * y * sin4l0 - 1.25 * e * e * sin2m;

        return radToDeg( Etime ) * 4.0; // in minutes of time
    }

    // Return the hour angle for given location, declination, and time of day
    function calcHourAngle( time, longitude, eqtime ) {
        return ( 15.0 * ( time - ( longitude / 15.0 ) - ( eqtime / 60.0 ) ) );
        // in degrees
    }

    // Returns decimal latitude from degree
    function getLatitude( thePlace ) {
        var neg = 0;
        var degs = parseFloat( thePlace.latDeg );
        if ( thePlace.latDeg[ 0 ] == '-' ) {
            neg = 1;
        }

        var mins = parseFloat( thePlace.latMin );

        var secs = parseFloat( thePlace.latSec );

        if ( neg != 1 ) {
            var decLat = degs + ( mins / 60 ) + ( secs / 3600 );
        } else if ( neg == 1 ) {
            var decLat = degs - ( mins / 60 ) - ( secs / 3600 );
        } else {
            return -9999
        }
        return decLat;
    }

    // Returns decimal longitude from degree
    function getLongitude( thePlace ) {
        var neg = 0;
        var degs = parseFloat( thePlace.lonDeg );
        if ( thePlace.lonDeg[ 0 ] == '-' ) {
            neg = 1;
        }

        var mins = parseFloat( thePlace.lonMin );

        var secs = parseFloat( thePlace.lonSec );

        if ( neg != 1 ) {
            var decLon = degs + ( mins / 60 ) + ( secs / 3600 );
        } else if ( neg == 1 ) {
            var decLon = degs - ( mins / 60 ) - ( secs / 3600 );
        } else {
            return -9999
        }
        return decLon;
    }

    //*************************************


    //*************************************
    //****  Main calculation routine  *****
    //*************************************

    // Calculate the solar position for the specific date, time, and location.
    // 	Results are reported in azimuth and elevation (in degrees) and cosine
    //	  of solar zenith angle.

    function calcSun( theHour, thePlace ) {
        var latitude = getLatitude( thePlace );
        var longitude = getLongitude( thePlace );

        // Get calc solar date/time
        var julDay = calcJD( parseFloat( theHour.year ), parseFloat( theHour.month ), parseFloat( theHour.day ) );
        var zone = parseFloat( thePlace.zoneHr );
        var daySavings = parseFloat( thePlace.dst );

        var hh = parseFloat( theHour.hour ) - ( daySavings / 60 );
        while ( hh > 23 ) {
            hh -= 24;
        }
        theHour.hour = hh + ( daySavings / 60 );

        // timenow is GMT time for calculation
        var timenow = hh + zone;

        var JD = ( calcJD( parseFloat( theHour.year ), parseFloat( theHour.month ), parseFloat( theHour.day ) ) );
        var doy = calcDayOfYear( parseFloat( theHour.month ), parseFloat( theHour.day ), isLeapYear( theHour.year ) );
        var T = calcTimeJulianCent( JD + timenow / 24.0 );
        var R = calcSunRadVector( T );
        var alpha = calcSunRtAscension( T );
        var theta = calcSunDeclination( T );
        var Etime = calcEquationOfTime( T );

        var eqTime = Etime; // in minutes
        var solarDec = theta; // in degrees
        var earthRadVec = R;

        theHour.eqTime = ( Math.floor( 100 * eqTime ) ) / 100;
        theHour.solarDec = ( Math.floor( 100 * ( solarDec ) ) ) / 100;

        var solarTimeFix = eqTime - 4.0 * longitude + 60.0 * zone;
        var trueSolarTime = hh * 60.0 + solarTimeFix; // in minutes

        while ( trueSolarTime > 1440 ) {
            trueSolarTime -= 1440;
        }

        var hourAngle = trueSolarTime / 4.0 - 180.0;

        if ( hourAngle < -180 ) {
            hourAngle += 360.0;
        }

        var haRad = degToRad( hourAngle );

        var csz = Math.sin( degToRad( latitude ) ) * Math.sin( degToRad( solarDec ) ) + Math.cos( degToRad( latitude ) ) * Math.cos( degToRad( solarDec ) ) * Math.cos( haRad );
        if ( csz > 1.0 ) {
            csz = 1.0;
        } else if ( csz < -1.0 ) {
            csz = -1.0;
        }
        var zenith = radToDeg( Math.acos( csz ) );

        var azDenom = ( Math.cos( degToRad( latitude ) ) * Math.sin( degToRad( zenith ) ) );
        if ( Math.abs( azDenom ) > 0.001 ) {
            var azRad = ( ( Math.sin( degToRad( latitude ) ) * Math.cos( degToRad( zenith ) ) ) - Math.sin( degToRad( solarDec ) ) ) / azDenom;
            if ( Math.abs( azRad ) > 1.0 ) {
                if ( azRad < 0 ) {
                    azRad = -1.0;
                } else {
                    azRad = 1.0;
                }
            }

            var azimuth = 180.0 - radToDeg( Math.acos( azRad ) );

            if ( hourAngle > 0.0 ) {
                azimuth = -azimuth;
            }
        } else {
            if ( latitude > 0.0 ) {
                azimuth = 180.0;
            } else {
                azimuth = 0.0;
            }
        }
        if ( azimuth < 0.0 ) {
            azimuth += 360.0;
        }

        var exoatmElevation = 90.0 - zenith;
        if ( exoatmElevation > 85.0 ) {
            var refractionCorrection = 0.0;
        } else {
            var te = Math.tan( degToRad( exoatmElevation ) );
            if ( exoatmElevation > 5.0 ) {
                refractionCorrection = 58.1 / te - 0.07 / ( te * te * te ) +
                    0.000086 / ( te * te * te * te * te );
            } else if ( exoatmElevation > -0.575 ) {
                refractionCorrection = 1735.0 + exoatmElevation *
                    ( -518.2 + exoatmElevation * ( 103.4 +
                        exoatmElevation * ( -12.79 +
                            exoatmElevation * 0.711 ) ) );
            } else {
                refractionCorrection = -20.774 / te;
            }
            refractionCorrection = refractionCorrection / 3600.0;
        }

        var solarZen = zenith - refractionCorrection;

        if ( solarZen < 108.0 ) { // astronomical twilight
            theHour.azimuth = ( Math.floor( 100 *
                azimuth ) ) / 100;
            theHour.elevation = ( Math.floor( 100 *
                ( 90.0 - solarZen ) ) ) / 100;
            if ( solarZen < 90.0 ) {
                theHour.coszen =
                    ( Math.floor( 10000.0 * ( Math.cos( degToRad( solarZen ) ) ) ) ) / 10000.0;
            } else {
                theHour.coszen = 0.0;
            }
        } else { // do not report az & el after astro twilight
            theHour.azimuth = 0.0;
            theHour.elevation = ( Math.floor( 100 *
                ( 90.0 - solarZen ) ) ) / 100;
            theHour.coszen = 0.0;
        }


        return [ theHour.hour, theHour.day, ( theHour.month - 1 ), theHour.year, theHour.azimuth, theHour.elevation, theHour.eqTime, theHour.solarDec, theHour.coszen ];
    };
} );
