shader_type canvas_item;
render_mode unshaded;

uniform float wave_speed = 0.72;
uniform float wave_strength = 0.0012;
uniform vec4 highlight_color : source_color = vec4(0.34, 0.76, 0.86, 1.0);

void fragment() {
	vec2 wave_uv = UV;
	wave_uv.x += sin(TIME * wave_speed + UV.y * 18.0) * wave_strength;
	wave_uv.y += cos(TIME * wave_speed * 0.62 + UV.x * 14.0) * wave_strength * 0.38;
	vec4 color = texture(TEXTURE, wave_uv);
	float shimmer = max(0.0, sin(TIME * 1.1 + UV.x * 24.0 + UV.y * 15.0)) * 0.018;
	color.rgb = mix(color.rgb, highlight_color.rgb, shimmer);
	COLOR = color * COLOR;
}
