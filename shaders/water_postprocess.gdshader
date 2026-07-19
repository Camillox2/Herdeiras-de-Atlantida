shader_type canvas_item;
render_mode unshaded;

uniform sampler2D screen_texture : hint_screen_texture, repeat_disable, filter_linear;
uniform float water_top : hint_range(0.0, 1.0) = 0.75;
uniform float motion_strength : hint_range(0.0, 0.006) = 0.0018;

void fragment() {
	vec2 screen_uv = SCREEN_UV;
	vec4 base = textureLod(screen_texture, screen_uv, 0.0);
	float below_surface = smoothstep(water_top, water_top + 0.018, screen_uv.y);
	float cyan_bias = ((base.g + base.b) * 0.5) - base.r;
	float aquatic_color = smoothstep(0.055, 0.22, cyan_bias);
	float mask = below_surface * aquatic_color;

	float broad_wave = sin(screen_uv.y * 54.0 + TIME * 1.15) + sin(screen_uv.x * 37.0 - TIME * 0.72) * 0.55;
	float fine_wave = cos(screen_uv.x * 83.0 + screen_uv.y * 29.0 + TIME * 1.72);
	vec2 offset = vec2(broad_wave, fine_wave * 0.52) * motion_strength * mask;
	vec4 refracted = textureLod(screen_texture, clamp(screen_uv + offset, vec2(0.001), vec2(0.999)), 0.0);

	float caustic = pow(max(0.0, sin(screen_uv.x * 76.0 - TIME * 0.85) * sin(screen_uv.y * 41.0 + TIME * 0.62)), 5.0);
	refracted.rgb += vec3(0.035, 0.075, 0.085) * caustic * mask;
	COLOR = mix(base, refracted, mask * 0.88);
}
