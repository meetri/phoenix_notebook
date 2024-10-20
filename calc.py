# calculate new moons between a ranges of dates by finding the conjunction of the sun and moon.
def find_new_moon_conjunctions(swe, start_jd, end_jd):
    conjunction_times = []  # List to store the conjunction times

    while start_jd <= end_jd:
        sun_long = swe.calc_ut(start_jd, swe.SUN, flags=swe.FLG_SWIEPH)[0][0]
        moon_long = swe.calc_ut(start_jd, swe.MOON, flags=swe.FLG_SWIEPH)[0][0]

        # Calculate the difference in longitudes
        diff = (moon_long - sun_long) % 360

        # If the difference is small enough, we consider it a conjunction
        if abs(diff) > 360 - 0.0000001:  # The threshold can be adjusted
            # swe.jdut1_to_utc(start_jd)
            conjunction_times.append(start_jd)
            start_jd += 1

        # Increment the Julian day based on the difference in longitudes:
        start_jd += ((360 - diff)/360) * 19

    return conjunction_times