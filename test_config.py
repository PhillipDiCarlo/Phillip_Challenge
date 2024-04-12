import unittest
import requests

class TestServerConfiguration(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://d30y2nrmo4k3y3.cloudfront.net"

    def test_http_redirection(self):
        """Test HTTP to HTTPS redirection"""
        response = requests.get(self.base_url, allow_redirects=True)
        
        # Check if the final URL (after redirections) is HTTPS
        self.assertTrue(response.url.startswith("https://"),
                        msg="HTTP not redirected to HTTPS")

    def test_site_reachability(self):
        """Test if the HTTPS site is reachable and returns a successful HTTP status"""
        response = requests.get(self.base_url.replace("http", "https"))
        
        self.assertEqual(response.status_code, 200,
                         msg="Site is not reachable or did not return a successful status")
        
    def test_no_redirect(self):
        """Test that directly accessing HTTP does not return a response without redirecting"""
        response = requests.get(self.base_url, allow_redirects=False)
        
        # This test expects a redirection status code, typically 301 or 302; it fails if it receives 200
        self.assertNotEqual(response.status_code, 200,
                            msg="HTTP request was unexpectedly successful without redirect")


if __name__ == "__main__":
    unittest.main()
