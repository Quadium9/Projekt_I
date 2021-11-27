from astropy import wcs


def draw_const(decs, recs, const_dec, const_rec):

    w = wcs.WCS(naxis=2)
    w.wcs.crpix = [const_dec, const_rec]
    w.wcs.cdelt = [1, 1]
    w.wcs.crval = [const_rec, const_dec]
    w.wcs.ctype = ["RA---STG", "DEC--STG"]
    x, y = w.wcs_world2pix(decs, recs, 100)
    print(x, y)
    w, z = w.wcs_world2pix(decs, recs, 0)

    return {'x': x, 'y': y}

