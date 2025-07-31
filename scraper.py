def fetch_case_data(case_type, case_number, year):
    # MOCK MODE: Returns fake data for a specific demo input
    if case_type.upper() == "CS" and case_number == "100" and year == "2022":
        data = {
            'parties': 'Aman Kumar vs Union of India',
            'filing_date': '05-Mar-2022',
            'next_hearing': '20-Sep-2025',
            'pdf_url': 'https://example.com/demo_court_order.pdf'
        }
        raw_response = "<html><body>Mock case response: Aman Kumar vs Union...</body></html>"
        return data, raw_response

    # All other inputs simulate no match found
    return None, "No data (mock mode only triggers on CS/100/2022)"
