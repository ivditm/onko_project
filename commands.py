table_pop_data_creat = '''
        CREATE TABLE IF NOT EXISTS population_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reason TEXT DEFAULT 'заболеваемость',
            region TEXT NOT NULL,
            table_name TEXT NOT NULL,
            effectif_total_all INTEGER NOT NULL,
            indice_gros_all REAL NOT NULL,
            indice_standart_all REAL NOT NULL,
            indice_error_all REAL NOT NULL,
            effectif_total_men INTEGER DEFAULT 0,
            indice_gros_men REAL DEFAULT 0,
            indice_standart_men REAL DEFAULT 0,
            indice_error_men REAL DEFAULT 0,
            effectif_total_femme INTEGER DEFAULT 0,
            indice_gros_femme REAL DEFAULT 0,
            indice_standart_femme REAL DEFAULT 0,
            indice_error_femme REAL DEFAULT 0,
            UNIQUE (region, table_name),
            CHECK (effectif_total_all >= 0
                    AND effectif_total_men >= 0
                    AND effectif_total_femme >= 0)
)'''
table_pop_data_creat_mort = '''
        CREATE TABLE IF NOT EXISTS mort_cancer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reason TEXT DEFAULT 'смертность',
            region TEXT NOT NULL,
            table_name TEXT NOT NULL,
            effectif_total_all INTEGER NOT NULL,
            indice_gros_all REAL NOT NULL,
            indice_standart_all REAL NOT NULL,
            indice_error_all REAL NOT NULL,
            effectif_total_men INTEGER DEFAULT 0,
            indice_gros_men REAL DEFAULT 0,
            indice_standart_men REAL DEFAULT 0,
            indice_error_men REAL DEFAULT 0,
            effectif_total_femme INTEGER DEFAULT 0,
            indice_gros_femme REAL DEFAULT 0,
            indice_standart_femme REAL DEFAULT 0,
            indice_error_femme REAL DEFAULT 0,
            UNIQUE (region, table_name),
            CHECK (effectif_total_all >= 0
                    AND effectif_total_men >= 0
                    AND effectif_total_femme >= 0)
)'''
table_pop_data_insert = '''
INSERT INTO {table}
          (
            region,
            table_name,
            effectif_total_all,
            indice_gros_all,
            indice_standart_all,
            indice_error_all,
            effectif_total_men,
            indice_gros_men,
            indice_standart_men,
            indice_error_men,
            effectif_total_femme,
            indice_gros_femme,
            indice_standart_femme,
            indice_error_femme
           )
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
table_state_cancer_creat = '''
        CREATE TABLE IF NOT EXISTS State_cancer
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        region TEXT NOT NULL,
        treatment_done INTEGER,
        treatment_done_per REAL,
        treatment_not_done INTEGER,
        treatment_not_done_per REAL,
        surgery_per REAL,
        medicinal_per REAL,
        mix_per REAL,
        chemo_radiation_per REAL,
        CONSTRAINT treatment_done_pos CHECK(treatment_done >= 0),
        CONSTRAINT treatment_not_done_pos CHECK(treatment_not_done >= 0),
        CONSTRAINT treatment_done_per_ch CHECK(
                    treatment_done_per >= 0 AND treatment_done_per <= 100),
        CONSTRAINT treatment_not_done_per_ch CHECK(
                    treatment_not_done_per >= 0 AND
                        treatment_not_done_per <= 100),
        CONSTRAINT surgery_per_ch CHECK(
                    surgery_per >= 0
                        AND surgery_per <= 100),
        CONSTRAINT medicinal_per_ch CHECK(
                    medicinal_per >= 0 AND medicinal_per <= 100),
        CONSTRAINT mix_per_ch CHECK(mix_per >= 0 AND mix_per <= 100),
        CONSTRAINT chemo_radiation_per_ch CHECK(
                    chemo_radiation_per >= 0 AND chemo_radiation_per <= 100)
                    )'''
table_state_cancer_insert = '''
                            INSERT INTO State_cancer
                                (name,
                                    region,
                                    treatment_done,
                                    treatment_done_per,
                                    treatment_not_done,
                                    treatment_not_done_per,
                                    surgery_per,
                                    medicinal_per,
                                    mix_per,
                                    chemo_radiation_per)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
table_state_help_57 = '''
        CREATE TABLE IF NOT EXISTS State_help_57
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        region TEXT NOT NULL,
        registered INTEGER NOT NULL,
        registered_act_per REAL NOT NULL,
        total_end_year INTEGER NOT NULL,
        total_end_year_on_100 REAL NOT NULL,
        more_5_year_total INTEGER NOT NULL,
        more_5_year_total_per REAL NOT NULL,
        index_cummul REAL NOT NULL,
        mortality REAL NOT NULL,
        registered_cancer INTEGER NOT NULL,
        diagnosis_conf_morphologically REAL NOT NULL,
        I_stade REAL NOT NULL,
        II_stade REAL NOT NULL,
        III_stade REAL NOT NULL,
        IV_stade REAL NOT NULL,
        not_found REAL NOT NULL,
        mortality_first_year REAL NOT NULL,
        CONSTRAINT registered_ch CHECK(registered >= 0),
        CONSTRAINT registered_act_per_ch CHECK(
                       registered_act_per >= 0 AND registered_act_per <= 100),
        CONSTRAINT more_5_year_total_per_ch CHECK(
                    more_5_year_total_per >= 0
                       AND more_5_year_total_per <= 100),
        CONSTRAINT total_end_year_ch CHECK(
                    total_end_year >= 0),
        CONSTRAINT total_end_year_on_100_ch CHECK(
                    total_end_year_on_100 >= 0),
        CONSTRAINT more_5_year_total_ch CHECK(
                    more_5_year_total >= 0),
        CONSTRAINT index_cummul_ch CHECK(index_cummul >= 0),
        CONSTRAINT mortality_ch CHECK(
                    mortality >= 0 AND mortality <= 100)
                    )
'''
table_state_help_57_insert = '''
                            INSERT INTO State_help_57
                                (name,
                                    region,
                                    registered,
                                    registered_act_per,
                                    total_end_year,
                                    total_end_year_on_100,
                                    more_5_year_total,
                                    more_5_year_total_per,
                                    index_cummul,
                                    mortality,
                                    registered_cancer,
                                    diagnosis_conf_morphologically,
                                    I_stade,
                                    II_stade,
                                    III_stade,
                                    IV_stade,
                                    not_found,
                                    mortality_first_year)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,
                                        ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
table_06_cr = '''CREATE TABLE IF NOT EXISTS urban_rural
(id INTEGER PRIMARY KEY AUTOINCREMENT,
region TEXT NOT NULL,
urban_abs_all REAL NOT NULL,
urban_abs_men REAL NOT NULL,
urban_abs_women REAL NOT NULL,
urban_rude_all REAL NOT NULL,
urban_rude_men REAL NOT NULL,
urban_rude_women REAL NOT NULL,
rural_abs_all REAL NOT NULL,
rural_abs_men REAL NOT NULL,
rural_abs_women REAL NOT NULL,
rural_rude_all REAL NOT NULL,
rural_rude_men REAL NOT NULL,
rural_rude_women REAL NOT NULL,
CHECK (urban_abs_all >= 0 AND
urban_abs_men >= 0 AND
urban_abs_women >= 0 AND
urban_rude_all >= 0 AND
urban_rude_men >= 0 AND
urban_rude_women >= 0 AND
rural_abs_all >= 0 AND
rural_abs_men >= 0 AND
rural_abs_women >= 0 AND
rural_rude_all >= 0 AND
rural_rude_men >= 0 AND
rural_rude_women >= 0)
)'''
table_06_ins = '''
INSERT INTO urban_rural
(region,
urban_abs_all,
urban_abs_men,
urban_abs_women,
urban_rude_all,
urban_rude_men,
urban_rude_women,
rural_abs_all,
rural_abs_men,
rural_abs_women,
rural_rude_all,
rural_rude_men,
rural_rude_women)
VALUES (?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?)
'''
table_07 = '''
CREATE TABLE IF NOT EXISTS InSitu2021 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region TEXT NOT NULL,
    total_detected INTEGER,
    per_100_first_detected INTEGER,
    cervix_abs_number INTEGER,
    per_100_cervix INTEGER,
    breast_abs_number INTEGER,
    per_100_breast INTEGER
);
'''
table_07_insert = '''INSERT INTO InSitu2021 (
    region,
    total_detected,
    per_100_first_detected,
    cervix_abs_number,
    per_100_cervix,
    breast_abs_number,
    per_100_breast
)
VALUES (
    ?, ?, ?, ?,
    ?, ?, ?);
'''
table_57_cr = '''
CREATE TABLE IF NOT EXISTS TreatmentData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    region TEXT NOT NULL,
    TreatmentRefusalAbsolute INT,
    TreatmentRefusalPercentage FLOAT,
    StageI_II_IncludedInRefusalAbsolute INT,
    StageI_II_IncludedInRefusalPercentage FLOAT,
    ContraindicationsAbsolute INT,
    ContraindicationsPercentage FLOAT,
    StageI_II_IncludedInContraAbsolute INT,
    StageI_II_IncludedInContraPercentage FLOAT,
    OutpatientOnlyTreatmentAbs INT,
    OutpatientOnlyTreatmentPer FLOAT,
    CompletedTreatmentMEDAbsolute INT,
    CompletedTreatmentMEDINCLGEM INT,
    CompletedTreatmentAbsoluteRadiation INT,
    DrugTreatmentEligible INT,
    DrugTreatmentReceived INT,
    DrugTreatmentReceivedPercentage FLOAT,
    RadiationEligible INT,
    RadiationReceived INT,
    RadiationReceivedPercentage FLOAT,
    CombinedEligible INT,
    CombinedReceived INT,
    CombinedReceivedPercentage FLOAT
);'''
table_57_insert = '''INSERT INTO TreatmentData (
    region,
    TreatmentRefusalAbsolute,
    TreatmentRefusalPercentage,
    StageI_II_IncludedInRefusalAbsolute,
    StageI_II_IncludedInRefusalPercentage,
    ContraindicationsAbsolute,
    ContraindicationsPercentage,
    StageI_II_IncludedInContraAbsolute,
    StageI_II_IncludedInContraPercentage,
    OutpatientOnlyTreatmentAbs,
    OutpatientOnlyTreatmentPer,
    CompletedTreatmentMEDAbsolute,
    CompletedTreatmentMEDINCLGEM,
    CompletedTreatmentAbsoluteRadiation,
    DrugTreatmentEligible,
    DrugTreatmentReceived,
    DrugTreatmentReceivedPercentage,
    RadiationEligible,
    RadiationReceived,
    RadiationReceivedPercentage,
    CombinedEligible,
    CombinedReceived,
    CombinedReceivedPercentage
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
view = '''
CREATE VIEW data AS
SELECT *
FROM population_data
LEFT JOIN mort_cancer ON population_data.region = mort_cancer.region
LEFT JOIN State_cancer ON population_data.region = State_cancer.region
LEFT JOIN State_help_57 ON population_data.region = State_help_57.region
LEFT JOIN urban_rural ON population_data.region = urban_rural.region
LEFT JOIN InSitu2021 ON population_data.region = InSitu2021.region
LEFT JOIN TreatmentData ON population_data.region = TreatmentData.region;
'''
