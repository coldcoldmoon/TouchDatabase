from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TouchFeature(db.Model):
    __tablename__ = 'touch_features'

    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(50))
    material = db.Column(db.Integer)
    trial = db.Column(db.Integer)
    label = db.Column(db.Integer)

    # 特征字段
    feature_Ts = db.Column(db.Float)
    feature_Fs = db.Column(db.Float)
    feature_Gs = db.Column(db.Float)
    feature_Gs_ch1 = db.Column(db.Float)
    feature_Gs_ch2 = db.Column(db.Float)
    feature_ZCRs = db.Column(db.Float)
    feature_slopes = db.Column(db.Float)
    feature_mu3s = db.Column(db.Float)
    feature_mu4s = db.Column(db.Float)
    feature_mu_frics = db.Column(db.Float)
    feature_AVG_normal_force = db.Column(db.Float)
    feature_Touch_time = db.Column(db.Float)
    feature_Roughness = db.Column(db.Float)
    feature_Friction_F = db.Column(db.Float)
    feature_STD_fric = db.Column(db.Float)
    feature_COV_fric = db.Column(db.Float)
    feature_ZCRs_CH1 = db.Column(db.Float)
    feature_ZCRs_CH2 = db.Column(db.Float)
    feature_slopes_fric = db.Column(db.Float)
    feature_STD_normal = db.Column(db.Float)
    feature_COV_normal = db.Column(db.Float)
    feature_F_Amp = db.Column(db.Float)
    feature_F_Amp_std = db.Column(db.Float)
    feature_F_Amp_cov = db.Column(db.Float)
    feature_F_max = db.Column(db.Float)
    feature_Press_angle = db.Column(db.Float)
    feature_Press_angle_std = db.Column(db.Float)

def create_tables_if_not_exist():
    db.create_all()