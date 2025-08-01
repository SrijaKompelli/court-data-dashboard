def fetch_case_data(case_type, case_number, year):
    if case_type == "CS" and case_number == "100" and year == "2022":
        data = {
            'parties': 'Aman Kumar vs Union of India',
            'filing_date': '05-Mar-2022',
            'next_hearing': '20-Sep-2025',
            'status': 'Pending',
            'pdf_url': 'https://example.com/demo_court_order.pdf'
        }
        raw_response = "<html>Mock response</html>"
        return data, raw_response
    return None, "No match"
