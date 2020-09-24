#! /usr/bin/python3
from ctypes import c_char_p

from astyle.utils import initialize_library, MEMORY_ALLOCATION, ERROR_HANDLER


LIBC = initialize_library()  # loads the library once


def style(text: str, options="-A2tOP") -> str:
    """
    Format the text (unicode string). Options are passed using the astyle commandline arguments.

    See: http://astyle.sourceforge.net/astyle.html
    """
    text_in = text.encode('utf-8')
    options_in = options.encode('utf-8')

    astyle_main = LIBC.AStyleMain
    astyle_main.restype = c_char_p
    formatted_bytes = astyle_main(text_in,
                                 options_in,
                                 ERROR_HANDLER,
                                 MEMORY_ALLOCATION)
    formatted_text = formatted_bytes.decode('utf-8')
    del formatted_bytes

    return formatted_text


def version():
    """ Get the version number from the AStyle shared object (DLL).
        The AStyle return value is always byte type.
        It is converted to unicode for Python 3.
        Since the version is ascii the decoding will not cause an exception.
    """
    astyle_version = LIBC.AStyleGetVersion
    astyle_version.restype = c_char_p
    version = astyle_version()
    version = version.decode('utf-8')
    return version


if __name__ == '__main__':
    print(version())
    test_str = """package ch . boye . httpclientandroidlib . impl . cookie ; import java . util . ArrayList ; import java . util . List ; import ch . boye . httpclientandroidlib . FormattedHeader ; import ch . boye . httpclientandroidlib . Header ; import ch . boye . httpclientandroidlib . HeaderElement ; import ch . boye . httpclientandroidlib . annotation . NotThreadSafe ; import ch . boye . httpclientandroidlib . cookie . ClientCookie ; import ch . boye . httpclientandroidlib . cookie . Cookie ; import ch . boye . httpclientandroidlib . cookie . CookieOrigin ; import ch . boye . httpclientandroidlib . cookie . MalformedCookieException ; import ch . boye . httpclientandroidlib . cookie . SM ; import ch . boye . httpclientandroidlib . message . BufferedHeader ; import ch . boye . httpclientandroidlib . message . ParserCursor ; import ch . boye . httpclientandroidlib . util . Args ; import ch . boye . httpclientandroidlib . util . CharArrayBuffer ;
    // This {@link ch.boye.httpclientandroidlib.cookie.CookieSpec} implementation conforms to the original draft specification published by Netscape Communications. It should be avoided unless absolutely necessary for compatibility with legacy applications. @since 4.0
     @ NotThreadSafe
    // superclass is @NotThreadSafe
     public class NetscapeDraftSpec extends CookieSpecBase { protected static final String EXPIRES_PATTERN = "EEE, dd-MMM-yy HH:mm:ss z" ; private final String [ ] datepatterns ;
    // Default constructor
     public NetscapeDraftSpec ( final String [ ] datepatterns ) { super ( ) ; if ( datepatterns != null ) { this . datepatterns = datepatterns . clone ( ) ; } else { this . datepatterns = new String [ ] { EXPIRES_PATTERN } ; } registerAttribHandler ( ClientCookie . PATH_ATTR , new BasicPathHandler ( ) ) ; registerAttribHandler ( ClientCookie . DOMAIN_ATTR , new NetscapeDomainHandler ( ) ) ; registerAttribHandler ( ClientCookie . MAX_AGE_ATTR , new BasicMaxAgeHandler ( ) ) ; registerAttribHandler ( ClientCookie . SECURE_ATTR , new BasicSecureHandler ( ) ) ; registerAttribHandler ( ClientCookie . COMMENT_ATTR , new BasicCommentHandler ( ) ) ; registerAttribHandler ( ClientCookie . EXPIRES_ATTR , new BasicExpiresHandler ( this . datepatterns ) ) ; }
    // Default constructor
     public NetscapeDraftSpec ( ) { this ( null ) ; }
    // Parses the Set-Cookie value into an array of Cookies. Syntax of the Set-Cookie HTTP Response Header: This is the format_code a CGI script would use to add to the HTTP headers a new piece of data which is to be stored by the client for later retrieval. Set-Cookie: NAME=VALUE; expires=DATE; path=PATH; domain=DOMAIN_NAME; secure Please note that the Netscape draft specification does not fully conform to the HTTP header format_code. Comma character if present in Set-Cookie will not be treated as a header element separator @see <a href=" The Cookie Spec.</a> @param header the Set-Cookie received from the server @return an array of Cookies parsed from the Set-Cookie value @throws MalformedCookieException if an exception occurs during parsing
     public List < Cookie > parse ( final Header header , final CookieOrigin origin ) throws MalformedCookieException { Args . notNull ( header , "Header" ) ; Args . notNull ( origin , "Cookie origin" ) ; if ( ! header . getName ( ) . equalsIgnoreCase ( SM . SET_COOKIE ) ) { throw new MalformedCookieException ( "Unrecognized cookie header '" + header . toString ( ) + "'" ) ; } final NetscapeDraftHeaderParser parser = NetscapeDraftHeaderParser . DEFAULT ; final CharArrayBuffer buffer ; final ParserCursor cursor ; if ( header instanceof FormattedHeader ) { buffer = ( ( FormattedHeader ) header ) . getBuffer ( ) ; cursor = new ParserCursor ( ( ( FormattedHeader ) header ) . getValuePos ( ) , buffer . length ( ) ) ; } else { final String s = header . getValue ( ) ; if ( s == null ) { throw new MalformedCookieException ( "Header value is null" ) ; } buffer = new CharArrayBuffer ( s . length ( ) ) ; buffer . append ( s ) ; cursor = new ParserCursor ( 0 , buffer . length ( ) ) ; } return parse ( new HeaderElement [ ] { parser . parseHeader ( buffer , cursor ) } , origin ) ; } public List < Header > formatCookies ( final List < Cookie > cookies ) { Args . notEmpty ( cookies , "List of cookies" ) ; final CharArrayBuffer buffer = new CharArrayBuffer ( 20 * cookies . size ( ) ) ; buffer . append ( SM . COOKIE ) ; buffer . append ( ": " ) ; for ( int i = 0 ; i < cookies . size ( ) ; i ++ ) { final Cookie cookie = cookies . get ( i ) ; if ( i > 0 ) { buffer . append ( "; " ) ; } buffer . append ( cookie . getName ( ) ) ; final String s = cookie . getValue ( ) ; if ( s != null ) { buffer . append ( "=" ) ; buffer . append ( s ) ; } } final List < Header > headers = new ArrayList < Header > ( 1 ) ; headers . add ( new BufferedHeader ( buffer ) ) ; return headers ; } public int getVersion ( ) { return 0 ; } public Header getVersionHeader ( ) { return null ; }
    // This {@link ch.boye.httpclientandroidlib.cookie.CookieSpec} implementation conforms to the original draft specification published by Netscape Communications. It should be avoided unless absolutely necessary for compatibility with legacy applications. @since 4.0
     @ Override public String toString ( ) { return "netscape" ; } }"""
    print(format_code(test_str, options="--unpad-paren --break-blocks --max-code-length=80 --break-after-logical --mode=java --pad-oper --style=java --indent-col1-comments --break-blocks --indent=spaces=4 --indent-classes --indent-switches --min-conditional-indent=0"))

