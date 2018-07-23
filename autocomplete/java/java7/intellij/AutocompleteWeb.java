import com.sun.net.httpserver.Headers;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.InetSocketAddress;
import java.net.URI;
import java.net.URLDecoder;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import mjson.Json;

public class AutocompleteWeb {
    private static final String HOSTNAME = "localhost";
    private static final int PORT = 8080;
    private static final int BACKLOG = 1;
    private static final String HEADER_CONTENT_TYPE = "Content-Type";
    private static final Charset CHARSET = StandardCharsets.UTF_8;
    private static final int STATUS_OK = 200;

    public static void main(final String... args) throws IOException {
        final HttpServer server = HttpServer.create(new InetSocketAddress(HOSTNAME, PORT), BACKLOG);
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange he) throws IOException {
                String responseBody = new String(Files.readAllBytes(Paths.get("autocomplete.html")));
                final byte[] rawResponseBody = responseBody.getBytes(CHARSET);
                he.sendResponseHeaders(STATUS_OK, rawResponseBody.length);
                he.getResponseBody().write(rawResponseBody);
                he.close();
            }
        });
        server.createContext("/search", new HttpHandler() {
            @Override
            public void handle(HttpExchange he) throws IOException {
                try {
                    final Headers headers = he.getResponseHeaders();
                    final Map<String, List<String>> requestParameters = getRequestParameters(he.getRequestURI());
                    String query = requestParameters.get("q").get(0);

                    // Process query
                    Json results = Json.make(Arrays.asList("result 1", "result 2"));

                    final String responseBody = "{\"query\": \"" + query + "\", \"results\": " + results.toString() + "}";
                    headers.set(HEADER_CONTENT_TYPE, String.format("application/json; charset=%s", CHARSET));
                    final byte[] rawResponseBody = responseBody.getBytes(CHARSET);
                    he.sendResponseHeaders(STATUS_OK, rawResponseBody.length);
                    he.getResponseBody().write(rawResponseBody);
                } finally {
                    he.close();
                }
            }
        });
        server.start();
        System.out.println("Started server on http://" + HOSTNAME + ":" + PORT);
    }

    private static Map<String, List<String>> getRequestParameters(final URI requestUri) {
        final Map<String, List<String>> requestParameters = new LinkedHashMap<>();
        final String requestQuery = requestUri.getRawQuery();
        if (requestQuery != null) {
            final String[] rawRequestParameters = requestQuery.split("[&;]", -1);
            for (final String rawRequestParameter : rawRequestParameters) {
                final String[] requestParameter = rawRequestParameter.split("=", 2);
                final String requestParameterName = decodeUrlComponent(requestParameter[0]);
                if (!requestParameters.containsKey(requestParameterName)) {
                    requestParameters.put(requestParameterName, new ArrayList<String>());
                }
                final String requestParameterValue = requestParameter.length > 1 ? decodeUrlComponent(requestParameter[1]) : null;
                requestParameters.get(requestParameterName).add(requestParameterValue);
            }
        }
        return requestParameters;
    }

    private static String decodeUrlComponent(final String urlComponent) throws InternalError {
        try {
            return URLDecoder.decode(urlComponent, CHARSET.name());
        } catch (final UnsupportedEncodingException ex) {
            throw new InternalError(ex.getMessage());
        }
    }
}
