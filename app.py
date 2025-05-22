from flask import Flask, render_template, jsonify, request, send_from_directory
from models import db, TouchFeature, create_tables_if_not_exist
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///touch_behavior.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

materials_dict = {
    1: '木板',
    2: '防水布',
    3: '魔术贴钩面',
    4: '帆布',
    5: '铝片',
    6: '人造草皮',
    7: '渔网+木板',
    8: '泡泡包装',
    9: '砂纸',
    10: '羊毛',
    11: '塑料片',
    12: '石块表面',
    13: '眼镜布',
    14: '闪光纸',
    15: 'EPDM泡沫',
    16: '塑料网络',
    17: '硅胶+海绵',
    18: '皮革',
    19: '纹理铝片',
    20: '瓷砖',
    21: '地毯',
    22: '海绵',
    23: '金闪纸',
    24: '毛毡',
    25: '冰丝'
}

# 在应用启动时手动创建表格
with app.app_context():
    create_tables_if_not_exist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/materials/<filename>')
def materials(filename):
    return send_from_directory('materials', filename)

@app.route('/api/touch-features', methods=['GET'])
def get_touch_features():
    person = request.args.get('person')
    material = request.args.get('material')

    query = TouchFeature.query
    if person:
        query = query.filter_by(person=person)
    if material:
        query = query.filter_by(material=material)

    results = query.all()

    features_list = []
    for feature in results:
        features_dict = {
            "id": feature.id,
            "person": feature.person,
            "material": feature.material,
            "material_name": materials_dict[int(feature.material)],
            "trial": feature.trial,
            "label": feature.label,
            "feature_Ts": feature.feature_Ts,
            "feature_Fs": feature.feature_Fs,
            "feature_Gs": feature.feature_Gs,
            "feature_Gs_ch1": feature.feature_Gs_ch1,
            "feature_Gs_ch2": feature.feature_Gs_ch2,
            "feature_ZCRs": feature.feature_ZCRs,
            "feature_slopes": feature.feature_slopes,
            "feature_mu3s": feature.feature_mu3s,
            "feature_mu4s": feature.feature_mu4s,
            "feature_mu_frics": feature.feature_mu_frics,
            "feature_AVG_normal_force": feature.feature_AVG_normal_force,
            "feature_Touch_time": feature.feature_Touch_time,
            "feature_Roughness": feature.feature_Roughness,
            "feature_Friction_F": feature.feature_Friction_F,
            "feature_STD_fric": feature.feature_STD_fric,
            "feature_COV_fric": feature.feature_COV_fric,
            "feature_ZCRs_CH1": feature.feature_ZCRs_CH1,
            "feature_ZCRs_CH2": feature.feature_ZCRs_CH2,
            "feature_slopes_fric": feature.feature_slopes_fric,
            "feature_STD_normal": feature.feature_STD_normal,
            "feature_COV_normal": feature.feature_COV_normal,
            "feature_F_Amp": feature.feature_F_Amp,
            "feature_F_Amp_std": feature.feature_F_Amp_std,
            "feature_F_Amp_cov": feature.feature_F_Amp_cov,
            "feature_F_max": feature.feature_F_max,
            "feature_Press_angle": feature.feature_Press_angle,
            "feature_Press_angle_std": feature.feature_Press_angle_std
        }
        features_list.append(features_dict)

    return jsonify(features_list)

if __name__ == '__main__':
    app.run(debug=True)