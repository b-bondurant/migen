from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform


_io = [
    # Clocks, UG1271 Table 3-17
    ("clk_125", 0,
        Subsignal("p", Pins("AL17"), IOStandard("LVDS")),
        Subsignal("n", Pins("AM17"), IOStandard("LVDS"))
    ),
    ("clk_100", 0,
        Subsignal("p", Pins("AM15"), IOStandard("LVDS")),
        Subsignal("n", Pins("AN15"), IOStandard("LVDS"))
    ),
    # U47
    ("user_si570", 0,
        Subsignal("p", Pins("J19"), IOStandard("DIFF_POD12")),
        Subsignal("n", Pins("J18"), IOStandard("DIFF_POD12"))
    ),
    # U49
    ("user_mgt_si570", 0,
        Subsignal("p", Pins("V31")),
        Subsignal("n", Pins("V32"))
    ),
    # J14/15
    ("user_sma_mgt_clock", 0,
        Subsignal("p", Pins("T31")),
        Subsignal("n", Pins("T32"))
    ),
    # U48
    ("sfp_si5382_in1", 0,
        Subsignal("p", Pins("AA33")),
        Subsignal("n", Pins("AA34"))
    ),
    ("sfp_si5382_out", 0,
        Subsignal("p", Pins("Y31")),
        Subsignal("n", Pins("Y32"))
    ),
    ("sfp_rec_clock", 0,
        Subsignal("p", Pins("AW14"), IOStandard("LVDS")),
        Subsignal("n", Pins("AW13"), IOStandard("LVDS"))
    ),
    # U90
    ("sysref_fpga_c", 0,
        Subsignal("p", Pins("AK17"), IOStandard("LVDS")),
        Subsignal("n", Pins("AK16"), IOStandard("LVDS"))
    ),
    ("fpga_refclk_out_c", 0,
        Subsignal("p", Pins("AL16"), IOStandard("LVDS")),
        Subsignal("n", Pins("AL15"), IOStandard("LVDS"))
    ),

    # RFMC ADC connector, UG1271 Figures 3-21, D-4, D-5
    ("adcio", 0, Pins("AP5"), IOStandard("LVCMOS18")),
    ("adcio", 1, Pins("AP6"), IOStandard("LVCMOS18")),
    ("adcio", 2, Pins("AR6"), IOStandard("LVCMOS18")),
    ("adcio", 3, Pins("AR7"), IOStandard("LVCMOS18")),
    ("adcio", 4, Pins("AV7"), IOStandard("LVCMOS18")),
    ("adcio", 5, Pins("AU7"), IOStandard("LVCMOS18")),
    ("adcio", 6, Pins("AV8"), IOStandard("LVCMOS18")),
    ("adcio", 7, Pins("AU8"), IOStandard("LVCMOS18")),
    ("adcio", 8, Pins("AT6"), IOStandard("LVCMOS18")),
    ("adcio", 9, Pins("AT7"), IOStandard("LVCMOS18")),
    ("adcio", 10, Pins("AU5"), IOStandard("LVCMOS18")),
    ("adcio", 11, Pins("AT5"), IOStandard("LVCMOS18")),
    ("adcio", 12, Pins("AU3"), IOStandard("LVCMOS18")),
    ("adcio", 13, Pins("AU4"), IOStandard("LVCMOS18")),
    ("adcio", 14, Pins("AV5"), IOStandard("LVCMOS18")),
    ("adcio", 15, Pins("AV6"), IOStandard("LVCMOS18")),
    ("adcio", 16, Pins("AU1"), IOStandard("LVCMOS18")),
    ("adcio", 17, Pins("AU2"), IOStandard("LVCMOS18")),
    ("adcio", 18, Pins("AV2"), IOStandard("LVCMOS18")),
    ("adcio", 19, Pins("AV3"), IOStandard("LVCMOS18")),
    # Bank 224
    ("rf1_clko_a_c", 0,
        Subsignal("n", Pins("AF4")),
        Subsignal("p", Pins("AF5"))
    ),
    ("vcm_01_224", 0, Pins("AL5")),
    ("vcm_23_224", 0, Pins("AL4")),
    ("rfmc_adc", 0,
        Subsignal("n", Pins("AP1")),
        Subsignal("p", Pins("AP2"))
    ),
    ("rfmc_adc", 1,
        Subsignal("n", Pins("AM1")),
        Subsignal("p", Pins("AM2"))
    ),
    # Bank 225
    ("rf1_clko_b_c", 0,
        Subsignal("n", Pins("AD4")),
        Subsignal("p", Pins("AD5"))
    ),
    ("vcm_01_225", 0, Pins("AK5")),
    ("vcm_23_225", 0, Pins("AK4")),
    ("rfmc_adc", 2,
        Subsignal("n", Pins("AK1")),
        Subsignal("p", Pins("AK2"))
    ),
    ("rfmc_adc", 3,
        Subsignal("n", Pins("AH1")),
        Subsignal("p", Pins("AH2"))
    ),
    # Bank 226
    ("rf2_clko_b_c", 0,
        Subsignal("n", Pins("AB4")),
        Subsignal("p", Pins("AB5"))
    ),
    ("vcm_01_226", 0, Pins("AJ5")),
    ("vcm_23_226", 0, Pins("AJ4")),
    ("rfmc_adc", 4,
        Subsignal("n", Pins("AF1")),
        Subsignal("p", Pins("AF2"))
    ),
    ("rfmc_adc", 5,
        Subsignal("n", Pins("AD1")),
        Subsignal("p", Pins("AD2"))
    ),
    # Bank 227
    ("rf2_clko_a_c", 0,
        Subsignal("n", Pins("Y4")),
        Subsignal("p", Pins("Y5"))
    ),
    ("vcm_01_227", 0, Pins("AH5")),
    ("vcm_23_227", 0, Pins("AH4")),
    ("rfmc_adc", 6,
        Subsignal("n", Pins("AB1")),
        Subsignal("p", Pins("AB2"))
    ),
    ("rfmc_adc", 7,
        Subsignal("n", Pins("Y1")),
        Subsignal("p", Pins("Y2"))
    ),

    # RFMC DAC connector, UG1271 Figures 3-22, D-4, D-5
    ("dacio", 0, Pins("A9"), IOStandard("LVCMOS18")),
    ("dacio", 1, Pins("A10"), IOStandard("LVCMOS18")),
    ("dacio", 2, Pins("A6"), IOStandard("LVCMOS18")),
    ("dacio", 3, Pins("A7"), IOStandard("LVCMOS18")),
    ("dacio", 4, Pins("A5"), IOStandard("LVCMOS18")),
    ("dacio", 5, Pins("B5"), IOStandard("LVCMOS18")),
    ("dacio", 6, Pins("C5"), IOStandard("LVCMOS18")),
    ("dacio", 7, Pins("C6"), IOStandard("LVCMOS18")),
    ("dacio", 8, Pins("B9"), IOStandard("LVCMOS18")),
    ("dacio", 9, Pins("B10"), IOStandard("LVCMOS18")),
    ("dacio", 10, Pins("B7"), IOStandard("LVCMOS18")),
    ("dacio", 11, Pins("B8"), IOStandard("LVCMOS18")),
    ("dacio", 12, Pins("D8"), IOStandard("LVCMOS18")),
    ("dacio", 13, Pins("D9"), IOStandard("LVCMOS18")),
    ("dacio", 14, Pins("C7"), IOStandard("LVCMOS18")),
    ("dacio", 15, Pins("C8"), IOStandard("LVCMOS18")),
    ("dacio", 16, Pins("C10"), IOStandard("LVCMOS18")),
    ("dacio", 17, Pins("D10"), IOStandard("LVCMOS18")),
    ("dacio", 18, Pins("D6"), IOStandard("LVCMOS18")),
    ("dacio", 19, Pins("E7"), IOStandard("LVCMOS18")),
    # Bank 228
    ("rf3_clko_a_c", 0,
        Subsignal("n", Pins("R4")),
        Subsignal("p", Pins("R5"))
    ),
    ("sysref_rfsoc_c", 0,
        Subsignal("n", Pins("U4")),
        Subsignal("p", Pins("U5"))
    ),
    ("rfmc_dac", 0,
        Subsignal("n", Pins("U1")),
        Subsignal("p", Pins("U2"))
    ),
    ("rfmc_dac", 1,
        Subsignal("n", Pins("R1")),
        Subsignal("p", Pins("R2"))
    ),
    ("rfmc_dac", 2,
        Subsignal("n", Pins("N1")),
        Subsignal("p", Pins("N2"))
    ),
    ("rfmc_dac", 3,
        Subsignal("n", Pins("L1")),
        Subsignal("p", Pins("L2"))
    ),
    # Bank 229
    ("rf3_clko_b_c", 0,
        Subsignal("n", Pins("N4")),
        Subsignal("p", Pins("N5"))
    ),
    ("rfmc_dac", 4,
        Subsignal("n", Pins("J1")),
        Subsignal("p", Pins("J2"))
    ),
    ("rfmc_dac", 5,
        Subsignal("n", Pins("G1")),
        Subsignal("p", Pins("G2"))
    ),
    ("rfmc_dac", 6,
        Subsignal("n", Pins("E1")),
        Subsignal("p", Pins("E2"))
    ),
    ("rfmc_dac", 7,
        Subsignal("n", Pins("C1")),
        Subsignal("p", Pins("C2"))
    ),


    # SFP, UG1271 Table 3-22
    ("sfp", 0,
        Subsignal(
            "tx",
            Subsignal("p", Pins("Y35")),
            Subsignal("n", Pins("Y36"))
        ),
        Subsignal(
            "rx",
            Subsignal("p", Pins("AA38")),
            Subsignal("n", Pins("AA39"))
        ),
        Subsignal("tx_disable_b", Pins("G12"), IOStandard("LVCMOS12"))
    ),
    ("sfp", 1,
        Subsignal(
            "tx",
            Subsignal("p", Pins("V35")),
            Subsignal("n", Pins("V36"))
        ),
        Subsignal(
            "rx",
            Subsignal("p", Pins("W38")),
            Subsignal("n", Pins("W39"))
        ),
        Subsignal("tx_disable_b", Pins("G10"), IOStandard("LVCMOS12"))
    ),
    ("sfp", 2,
        Subsignal(
            "tx",
            Subsignal("p", Pins("T35")),
            Subsignal("n", Pins("T36"))
        ),
        Subsignal(
            "rx",
            Subsignal("p", Pins("U38")),
            Subsignal("n", Pins("U39"))
        ),
        Subsignal("tx_disable_b", Pins("K12"), IOStandard("LVCMOS12"))
    ),
    ("sfp", 3,
        Subsignal(
            "tx",
            Subsignal("p", Pins("R33")),
            Subsignal("n", Pins("R34"))
        ),
        Subsignal(
            "rx",
            Subsignal("p", Pins("R38")),
            Subsignal("n", Pins("R39"))
        ),
        Subsignal("tx_disable_b", Pins("J7"), IOStandard("LVCMOS12"))
    ),

    # PMOD, UG1271 Table 3-23
    ("pmod0", 0, Pins("C17"), IOStandard("LVCMOS12")),
    ("pmod0", 1, Pins("M18"), IOStandard("LVCMOS12")),
    ("pmod0", 2, Pins("H16"), IOStandard("LVCMOS12")),
    ("pmod0", 3, Pins("H17"), IOStandard("LVCMOS12")),
    ("pmod0", 4, Pins("J16"), IOStandard("LVCMOS12")),
    ("pmod0", 5, Pins("K16"), IOStandard("LVCMOS12")),
    ("pmod0", 6, Pins("H15"), IOStandard("LVCMOS12")),
    ("pmod0", 7, Pins("J15"), IOStandard("LVCMOS12")),

    ("pmod1", 0, Pins("L14"), IOStandard("LVCMOS12")),
    ("pmod1", 1, Pins("L15"), IOStandard("LVCMOS12")),
    ("pmod1", 2, Pins("M13"), IOStandard("LVCMOS12")),
    ("pmod1", 3, Pins("N13"), IOStandard("LVCMOS12")),
    ("pmod1", 4, Pins("M15"), IOStandard("LVCMOS12")),
    ("pmod1", 5, Pins("N15"), IOStandard("LVCMOS12")),
    ("pmod1", 6, Pins("M14"), IOStandard("LVCMOS12")),
    ("pmod1", 7, Pins("N14"), IOStandard("LVCMOS12")),

    # User GPIO, UG1271 Table 3-24
    ("gpio_led", 0, Pins("AR13"), IOStandard("LVCMOS18")),
    ("gpio_led", 1, Pins("AP13"), IOStandard("LVCMOS18")),
    ("gpio_led", 2, Pins("AR16"), IOStandard("LVCMOS18")),
    ("gpio_led", 3, Pins("AP16"), IOStandard("LVCMOS18")),
    ("gpio_led", 4, Pins("AP15"), IOStandard("LVCMOS18")),
    ("gpio_led", 5, Pins("AN16"), IOStandard("LVCMOS18")),
    ("gpio_led", 6, Pins("AN17"), IOStandard("LVCMOS18")),
    ("gpio_led", 7, Pins("AV15"), IOStandard("LVCMOS18")),

    ("gpio_dip_sw", 0, Pins("AF16"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 1, Pins("AF17"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 2, Pins("AH15"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 3, Pins("AH16"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 4, Pins("AH17"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 5, Pins("AG17"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 6, Pins("AJ15"), IOStandard("LVCMOS18")),
    ("gpio_dip_sw", 7, Pins("AJ16"), IOStandard("LVCMOS18")),

    ("gpio_sw_n", 0, Pins("AW3"), IOStandard("LVCMOS18")),
    ("gpio_sw_w", 0, Pins("AW6"), IOStandard("LVCMOS18")),
    ("gpio_sw_c", 0, Pins("AW5"), IOStandard("LVCMOS18")),
    ("gpio_sw_e", 0, Pins("AW4"), IOStandard("LVCMOS18")),
    ("gpio_sw_s", 0, Pins("E8"), IOStandard("LVCMOS18")),

    # Not documented
    ("ams_fpga_ref_clk", 0, Pins("AP14"), IOStandard("LVCMOS18")),

    ("uart2", 0,
        Subsignal("cts_b", Pins("AT14"), IOStandard("LVCMOS18")),
        Subsignal("rts_b", Pins("AU14"), IOStandard("LVCMOS18")),
        Subsignal("rxd_fpga_txd", Pins("AU15"), IOStandard("LVCMOS18")),
        Subsignal("txd_fpga_rxd", Pins("AT15"), IOStandard("LVCMOS18"))
    ),

    ("pl_i2c", 0,
        Subsignal("scl", Pins("AT16"), IOStandard("LVCMOS18")),
        Subsignal("sda", Pins("AW16"), IOStandard("LVCMOS18"))
    ),
    ("pl_i2c", 1,
        Subsignal("scl", Pins("AV16"), IOStandard("LVCMOS18")),
        Subsignal("sda", Pins("AV13"), IOStandard("LVCMOS18"))
    ),

    ("sfp_si5382_clk_in_sel", 0, Pins("E9"), IOStandard("LVCMOS18")),

    # TODO: PL DDR4 pins (but MiSoC doesn't currently support DDR4)
]

_connectors = [
    ("FMCP_HSPC", {
        "LA32_N": "AF19",
        "LA32_P": "AF20",
        "LA33_N": "AH18",
        "LA33_P": "AG18",
        "LA30_N": "AH20",
        "LA30_P": "AG20",
        "LA31_N": "AJ19",
        "LA31_P": "AJ20",
        "LA29_N": "AK21",
        "LA29_P": "AK22",
        "LA28_N": "AK18",
        "LA28_P": "AJ18",
        "LA25_N": "AL20",
        "LA25_P": "AL21",
        "LA21_N": "AM19",
        "LA21_P": "AL19",
        "LA24_N": "AM22",
        "LA24_P": "AL22",
        "LA23_N": "AN18",
        "LA23_P": "AM18",
        "LA17_CC_N": "AP21",
        "LA17_CC_P": "AN21",
        "LA18_CC_N": "AN20",
        "LA18_CC_P": "AM20",
        "CLK1_M2C_N": "AP19",
        "CLK1_M2C_P": "AP20",
        "LA26_N": "AT22",
        "LA26_P": "AR22",
        "LA22_N": "AT19",
        "LA22_P": "AR19",
        "LA27_N": "AT21",
        "LA27_P": "AR21",
        "LA20_N": "AT17",
        "LA20_P": "AR17",
        "LA19_N": "AU19",
        "LA19_P": "AU20",
        "LA02_N": "AJ13",
        "LA02_P": "AH13",
        "LA04_N": "AH12",
        "LA04_P": "AG12",
        "LA15_N": "AK14",
        "LA15_P": "AJ14",
        "LA03_N": "AK12",
        "LA03_P": "AJ12",
        "LA14_N": "AM14",
        "LA14_P": "AL14",
        "LA07_N": "AL12",
        "LA07_P": "AK13",
        "LA06_N": "AL7",
        "LA06_P": "AL8",
        "LA08_N": "AM9",
        "LA08_P": "AL9",
        "LA09_N": "AN7",
        "LA09_P": "AN8",
        "LA05_N": "AM7",
        "LA05_P": "AM8",
        "LA00_CC_N": "AR9",
        "LA00_CC_P": "AP9",
        "LA01_CC_N": "AR8",
        "LA01_CC_P": "AP8",
        "CLK0_M2C_N": "AP10",
        "CLK0_M2C_P": "AN10",
        "REFCLK_M2C_N": "AP11",
        "REFCLK_M2C_P": "AN11",
        "LA13_N": "AN13",
        "LA13_P": "AM13",
        "LA12_N": "AM10",
        "LA12_P": "AL10",
        "LA16_N": "AR11",
        "LA16_P": "AR12",
        "LA10_N": "AN12",
        "LA10_P": "AM12",
        "LA11_N": "AU10",
        "LA11_P": "AT10",
        "SYNC_C2M_N": "AT11",
        "SYNC_C2M_P": "AT12",
        "REFCLK_C2M_N": "AW11",
        "REFCLK_C2M_P": "AV11",
        "SYNC_M2C_N": "AV12",
        "SYNC_M2C_P": "AU12",
        "GBTCLK0_M2C_C_N": "W34",
        "GBTCLK0_M2C_C_P": "W33",
        "DP0_M2C_N": "N39",
        "DP1_M2C_N": "M37",
        "DP2_M2C_N": "L39",
        "DP3_M2C_N": "K37",
        "DP0_M2C_P": "N38",
        "DP1_M2C_P": "M36",
        "DP2_M2C_P": "L38",
        "DP3_M2C_P": "K36",
        "DP0_C2M_N": "P36",
        "DP1_C2M_N": "N34",
        "DP2_C2M_N": "L34",
        "DP3_C2M_N": "J34",
        "DP0_C2M_P": "P35",
        "DP1_C2M_P": "N33",
        "DP2_C2M_P": "L33",
        "DP3_C2M_P": "J33",
        "GBTCLK1_M2C_C_N": "U34",
        "GBTCLK1_M2C_C_P": "U33",
        "DP4_M2C_N": "J39",
        "DP5_M2C_N": "H37",
        "DP6_M2C_N": "G39",
        "DP7_M2C_N": "F37",
        "DP4_M2C_P": "J38",
        "DP5_M2C_P": "H36",
        "DP6_M2C_P": "G38",
        "DP7_M2C_P": "F36",
        "DP4_C2M_N": "H32",
        "DP5_C2M_N": "G34",
        "DP6_C2M_N": "F32",
        "DP7_C2M_N": "E34",
        "DP4_C2M_P": "H31",
        "DP5_C2M_P": "G33",
        "DP6_C2M_P": "F31",
        "DP7_C2M_P": "E33",
        "GBTCLK2_M2C_C_N": "P32",
        "GBTCLK2_M2C_C_P": "P31",
        "DP8_M2C_N": "E39",
        "DP9_M2C_N": "D37",
        "DP10_M2C_N": "C39",
        "DP11_M2C_N": "B37",
        "DP8_M2C_P": "E38",
        "DP9_M2C_P": "D36",
        "DP10_M2C_P": "C38",
        "DP11_M2C_P": "B36",
        "DP8_C2M_N": "D32",
        "DP9_C2M_N": "C34",
        "DP10_C2M_N": "B32",
        "DP11_C2M_N": "A34",
        "DP8_C2M_P": "D31",
        "DP9_C2M_P": "C33",
        "DP10_C2M_P": "B31",
        "DP11_C2M_P": "A33",
    })
]


class Platform(XilinxPlatform):
    default_clk_name = "clk_125"
    default_clk_period = 8

    def __init__(self):
        XilinxPlatform.__init__(self, "xczu28dr-2ffvg1517e", _io, _connectors,
                                toolchain="vivado")
