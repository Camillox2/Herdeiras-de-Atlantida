shader_type canvas_item;
render_mode unshaded;

uniform float wave_speed = 1.35;
uniform float wave_strength = 0.0025;
uniform vec4 highlight_color : source_color = vec4(0.38, 0.84, 0.94, 1.0);

void fragment() {
	vec2 wave_uv = UV;
	wave_uv.x += sin(TIME * wave_speed + UV.y * 30.0) * wave_strength;
	wave_uv.y += cos(TIME * wave_speed * 0.7 + UV.x * 22.0) * wave_strength * 0.45;
	vec4 color = texture(TEXTURE, wave_uv);
	float shimmer = max(0.0, sin(TIME * 1.8 + UV.x * 42.0 + UV.y * 26.0)) * 0.035;
	color.rgb = mix(color.rgb, highlight_color.rgb, shimmer);
	COLOR = color * COLOR;
}
