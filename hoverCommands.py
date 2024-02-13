#     Type 	      Name 	        Description 	                             Can be Set 	Can be saved to EEPROM
#   Parameter 	CTRL_MOD 	    Ctrl mode 1:Voltage 2:Speed 3:Torque 	            Yes 	No
#   Parameter 	CTRL_TYP 	    Ctrl type 0:Commutation 1:Sinusoidal 2:FOC 	        Yes 	No
#   Parameter 	I_MOT_MAX 	    Max phase current A 	                            Yes 	Yes
#   Parameter 	N_MOT_MAX 	    Max motor RPM 	                                    Yes 	Yes
#   Parameter 	FI_WEAK_ENA 	Enable field weak 0:OFF 1:ON 	                    Yes 	No
#   Parameter 	FI_WEAK_HI 	    Field weak high RPM 	                            Yes 	No
#   Parameter 	FI_WEAK_LO 	    Field weak low RPM 	                                Yes 	No
#   Parameter 	FI_WEAK_MAX     Field weak max current A(FOC only) 	                Yes 	No
#   Parameter 	PHA_ADV_MAX 	Max Phase Adv angle Deg(SIN only) 	                Yes 	No
#   Variable 	IN1_RAW         Input1 raw value 	                                No     	No
#   Parameter 	IN1_TYP 	    Input1 type 0:Disabled, 1:Normal Pot,
#                               2:Middle Resting Pot, 3:Auto-detect 	            Yes 	Yes
#   Parameter 	IN1_MIN 	    Input1 minimum value 	                            Yes 	Yes
#   Parameter 	IN1_MID 	    Input1 middle value 	                            Yes 	Yes
#   Parameter 	IN1_MAX 	    Input1 maximum value 	                            Yes 	Yes
#   Variable 	IN1_CMD 	    Input1 command value 	                            No 	    No
#   Variable 	IN2_RAW 	    Input2 raw value 	                                No 	    No
#   Parameter 	IN2_TYP 	    Input2 type 0:Disabled, 1:Normal Pot,
#                               2:Middle Resting Pot, 3:Auto-detect 	            Yes 	Yes
#   Parameter 	IN2_MIN 	    Input2 minimum value 	                            Yes 	Yes
#   Parameter 	IN2_MID 	    Input2 middle value 	                            Yes 	Yes
#   Parameter 	IN2_MAX 	    Input2 maximum value 	                            Yes 	Yes
#   Variable 	IN2_CMD 	    Input2 command value 	                            No 	    No
#   Variable 	DC_CURR 	    Total DC Link current A *100 	                    No 		No
#   Variable 	LDC_CURR 	    Left DC Link current A *100 	                    No 		No
#   Variable 	RDC_CURR 	    Right DC Link current A *100 	                    No 		No
#   Variable 	CMDL 	        Left Motor Command RPM 	                            No 		No
#   Variable 	CMDR 	        Right Motor Command RPM 	                        No 		No
#   Variable 	SPD_AVG 	    Motor Measured Avg RPM 	                            No 		No
#   Variable 	SPDL 	        Left Motor Measured RPM 	                        No 		No
#   Variable 	SPDR 	        Right Motor Measured RPM 	                        No 		No
#   Variable 	RATE 	        Rate *10 	                                        No 		No
#   Variable 	SPD_COEF 	    Speed Coefficient *10 	                            No 		No
#   Variable 	STR_COEF 	    Steer Coefficient *10 	                            No 		No
#   Variable 	BATV 	        Calibrated Battery Voltage *100 	                No 		No
#   Variable 	TEMP 	        Calibrated Temperature °C *10 	                    No 		No

class HvrCmmndsClass:
    def __init__(self):
        self.par_ctrl_mod = 0       #Ctrl mode 1:Voltage 2:Speed 3:Torque 	            Yes 	No
        self.par_ctrl_typ = 0       #Ctrl type 0:Commutation 1:Sinusoidal 2:FOC 	    Yes 	No
        self.par_i_mot_max = 0      #Max phase current A 	                            Yes 	Yes
        self.par_n_mot_max  = 0     #Max motor RPM 	                                    Yes 	Yes
        self.par_fi_weak_ena = 0    #Enable field weak 0:OFF 1:ON 	                    Yes 	No
        self.par_fi_weak_hi  = 0    #Field weak high RPM 	                            Yes 	No
        self.par_fi_weak_lo  = 0    #Field weak low RPM 	                            Yes 	No
        self.par_fi_weak_max  = 0   #Field weak max current A(FOC only) 	            Yes 	No
        self.par_pha_adv_max = 0    #Max Phase Adv angle Deg(SIN only) 	                Yes 	No
        self.var_in1_raw = 0        #Input1 raw value 	                                No     	No
        self.par_in1_typ = 0        #Input1 type 0:Disabled, 1:Normal Pot,
                                    #2:Middle Resting Pot, 3:Auto-detect 	            Yes 	Yes
        self.par_in1_min = 0        #Input1 minimum value 	                            Yes 	Yes
        self.par_in1_mid = 0        #Input1 middle value 	                            Yes 	Yes
        self.par_in1_max = 0        #Input1 maximum value 	                            Yes 	Yes
        self.var_in1_cmd = 0        #Input1 command value 	                            No 	    No
        self.var_in2_raw = 0        #Input2 raw value 	                                No 	    No
        self.par_in2_typ = 0        #Input2 type 0:Disabled, 1:Normal Pot,
                                    #2:Middle Resting Pot, 3:Auto-detect 	            Yes 	Yes
        self.par_in2_min = 0        #Input2 minimum value 	                            Yes 	Yes
        self.par_in2_mid = 0        #Input2 middle value 	                            Yes 	Yes
        self.par_in2_max = 0        #Input2 maximum value 	                            Yes 	Yes
        self.var_in2_cmd = 0        #Input2 command value 	                            No 	    No
        self.var_dc_curr = 0        #Total DC Link current A *100 	                    No 		No
        self.var_ldc_curr = 0       #Left DC Link current A *100 	                    No 		No
        self.var_rdc_curr = 0       #Right DC Link current A *100 	                    No 		No
        self.var_cmdl = 0           #Left Motor Command RPM 	                        No 		No
        self.var_cmdr = 0           #Right Motor Command RPM 	                        No 		No
        self.var_spd_avg = 0        #Motor Measured Avg RPM 	                        No 		No
        self.var_spdl = 0           #Left Motor Measured RPM 	                        No 		No
        self.var_spdr = 0           #Right Motor Measured RPM 	                        No 		No
        self.var_rate = 0           #Rate *10 	                                        No 		No
        self.var_spd_coef = 0       #Speed Coefficient *10 	                            No 		No
        self.var_str_coef = 0       #Steer Coefficient *10 	                            No 		No
        self.var_batv = 0           #Calibrated Battery Voltage *100 	                No 		No
        self.var_temp = 0           #Calibrated Temperature °C *10 	                    No 		No
        self.hvrRpm = 0
        self.command = (
            "HELP",   #0
            "GET",    #1
            "SET",    #2
            "INIT",   #3
            "SAVE",   #4
            "WATHC"   #5
        )

        self.parametersDict = {
            "CTRL_MOD":     self.par_ctrl_mod,   #0
            "CTRL_TYP":     self.par_ctrl_typ,   #1
            "I_MOT_MAX":    self.par_i_mot_max,  #2
            "N_MOT_MAX":    self.par_n_mot_max,  #3
            "FI_WEAK_ENA":  self.par_fi_weak_ena,#4
            "FI_WEAK_HI":   self.par_fi_weak_hi, #5
            "FI_WEAK_LO":   self.par_fi_weak_lo, #6
            "FI_WEAK_MAX":  self.par_fi_weak_max,#7
            "PHA_ADV_MAX":  self.par_pha_adv_max,#8
            "IN1_RAW":      self.var_in1_raw,    #9
            "IN1_TYP":      self.par_in1_typ,    #10
            "IN1_MIN":      self.par_in1_min,    #11
            "IN1_MID":      self.par_in1_mid,    #12
            "IN1_MAX":      self.par_in1_max,    #13
            "IN1_CMD":      self.var_in1_cmd,    #14
            "IN2_RAW":      self.var_in2_raw,    #15
            "IN2_TYP":      self.par_in2_typ,    #16
            "IN2_MIN":      self.par_in2_min,    #17
            "IN2_MID":      self.par_in2_mid,    #18
            "IN2_MAX":      self.par_in2_max,    #19
            "IN2_CMD":      self.var_in2_cmd,    #20
            "DC_CURR":      self.var_dc_curr,    #21
            "LDC_CURR":     self.var_ldc_curr,   #22
            "RDC_CURR":     self.var_rdc_curr,   #23
            "CMDL":         self.var_cmdl,       #24
            "CMDR":         self.var_cmdr,       #25
            "SPD_AVG":      self.var_spd_avg,    #26
            "SPDL":         self.var_spdl,       #27
            "SPDR":         self.var_spdr,       #28
            "RATE":         self.var_rate,       #29
            "SPD_COEF":     self.var_spd_coef,   #30
            "STR_COEF":     self.var_str_coef,   #31
            "BATV":         self.var_batv,       #32
            "TEMP":         self.var_temp,       #33
        }
        self.parameters = (
            "CTRL_MOD",      #0
            "CTRL_TYP",      #1
            "I_MOT_MAX",     #2
            "N_MOT_MAX",     #3
            "FI_WEAK_ENA",   #4
            "FI_WEAK_HI",    #5
            "FI_WEAK_LO",    #6
            "FI_WEAK_MAX",   #7
            "PHA_ADV_MAX",   #8
            "IN1_RAW",       #9
            "IN1_TYP",       #10
            "IN1_MIN",       #11
            "IN1_MID",       #12
            "IN1_MAX",       #13
            "IN1_CMD",       #14
            "IN2_RAW",       #15
            "IN2_TYP",       #16
            "IN2_MIN",       #17
            "IN2_MID",       #18
            "IN2_MAX",       #19
            "IN2_CMD",       #20
            "DC_CURR",       #21
            "LDC_CURR",      #22
            "RDC_CURR",      #23
            "CMDL",          #24
            "CMDR",          #25
            "SPD_AVG",       #26
            "SPDL",          #27
            "SPDR",          #28
            "RATE",          #29
            "SPD_COEF",      #30
            "STR_COEF",      #31
            "BATV",          #32
            "TEMP"           #33
        )

    def get_parametr(self, parameter):
        self.command[1]
        print(self.command[1])
        print(self.parameters)
        print(self.parameters[0])

    def set_parametr(self, parameter):
        self.command[2]
        print(self.command[2])
        #print(self.parameters[:parameter])
