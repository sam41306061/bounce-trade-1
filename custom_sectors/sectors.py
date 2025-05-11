# region imports
from AlgorithmImports import *
# endregion


class SectorHandler:
    "Storing specific sector tickers based on personal project"
    def __init__(self):
        self.sectors = {
        "Realestate":[
            "PLD","AMT","WELL","EQIX","SPG","O","DLR","PSA",
            "CBRE","CCI","VICI","EXR","AVB","CSGP","VTR","IRM",
            "EQR","SBAC","WY","ESS","MAA","INVH","ARE","KIM","DOC",
            "UDR","CPT","REG","HST","BXP","FRT"
        ],
        "ConsumerStaples": [
            "COST","WMT","PG","KO","PM","PEP","MO","MDLZ","CL"
            ,"TGT","KMB","KVUE","KR","KDP","MNST","SYY","GIS","STZ",
            "CHD","KHC","HSY","ADM","K","MKC","CLX","TSN","EL","DG",
            "DLTR","CAG","SJM","TAP","BG","HRL","CPB","WBA","LW","BF.B"
        ],
        "Technology": [
            "AAPL","NVDA","MSFT","AVGO","CRM","ORCL","CSCO","IBM","ACN","ADBE","NOW","TXN",
            "QCOM","PLTR","INTU","AMD","AMAT","PANW","ADI","MU","INTC","LRCX","ANET","KLAC",
            "CRWD","APH","MSI","SNPS","FTNT","CDNS","ROP","ADSK","WDAY","NXPI","TEL","FICO",
            "CTSH","GLW","IT","MCHP","DELL","MPWR","HPQ","ANSS","KEYS","TYL","HPE","GDDY"
            "TDY","CDW","STX","SMCI","NTAP","ON","VRSN","PTC","TER","TRMB","JBL","FFIV","WDC",
            "ZBRA","GEN","FSLR","AKAM","JNPR","EPAM","SWKS","ENPH"
        ],
        "Industrial": [
                "CAT", "GE", "RTX", "UBER", "UNP", "HON", "ETN", "ADP", "DE", "BA",
                "LMT", "UPS", "TT", "PH", "GEV", "WM", "CTAS", "EMR", "ITW", "GD",
                "MMM", "CSX", "TDG", "FDX", "NOC", "CARR", "NSC", "PCAR", "URI", "CPRT",
                "JCI", "GWW", "CMI", "PWR", "FAST", "HWM", "PAYX", "LHX", "AME", "RSG",
                "AXON", "IR", "ODFL", "VRSK", "DAL", "OTIS", "WAB", "ROK", "EFX", "UAL",
                "XYL", "DOV", "FTV", "BR", "VLTO", "HUBB", "BLDR", "LDOS", "SNA", "LUV",
                "MAS", "IEX", "PNR", "J", "EXPD", "TXT", "JBHT", "ROL", "NDSN", "SWK",
                "DAY", "CHRW", "ALLE", "GNRC", "PAYC", "AOS", "HII"
            ],
        "Financial": [
                "JPM", "V", "MA", "BAC", "WFC", "GS", "AXP", "MS", "SPGI", "PGR",
                "BLK", "BX", "C", "FI", "SCHW", "MMC", "CB", "KKR", "ICE", "PYPL",
                "AON", "PNC", "USB", "CME", "MCO", "COF", "AJG", "TFC", "BK", "TRV",
                "AFL", "AMP", "ALL", "MET", "AIG", "MSCI", "FIS", "PRU", "DFS", "ACGL",
                "MTB", "HIG", "NDAQ", "FITB", "WTW", "RJF", "GPN", "STT", "TROW", "SYF",
                "CPAY", "BRO", "HBAN", "RF", "CINF", "CBOE", "NTRS", "CFG", "WRB", "FDS",
                "PFG", "KEY", "EG", "L", "JKHY", "AIZ", "ERIE", "GL", "MKTX", "IVZ", "BEN"
            ],
        "Energy": [
                "XOM", "CVX", "COP", "WMB", "OKE", "EOG", "SLB", "PSX", "KMI", "MPC",
                "VLO", "TRGP", "BKR", "HES", "OXY", "FANG", "HAL", "EQT", "TPL", "DVN",
                "CTRA", "APA"
            ],
        "HealthCare": [
                "LLY", "UNH", "JNJ", "ABBV", "MRK", "ABT", "TMO", "ISRG", "AMGN", "DHR",
                "PFE", "SYK", "BSX", "BMY", "VRTX", "GILD", "MDT", "ELV", "CI", "ZTS",
                "MCK", "REGN", "CVS", "BDX", "HCA", "EW", "COR", "A", "GEHC", "RMD",
                "HUM", "IQV", "IDXX", "CNC", "DXCM", "CAH", "MTD", "WST", "BIIB", "ZBH",
                "WAT", "STE", "COO", "LH", "PODD", "HOLX", "DGX", "MOH", "BAX", "ALGN",
                "VTRS", "MRNA", "RVTY", "UHS", "INCY", "TECH", "CTLT", "CRL", "SOLV",
                "HSIC", "TFX", "DVA"
            ]
    }


