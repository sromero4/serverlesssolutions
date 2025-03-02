import { defineStore } from "pinia";
import { ref, computed } from "vue";
import { layout } from "@/core/data/layout";
interface Settings {
    layout_type: string;
    layout: string;
    sidebar_icon: string;
    sidebar_setting: string;
}

interface Color {
    layout_version: string;
    primary_color: string;
    secondary_color: string;
}

interface AppConfig {
    settings: Settings;
    color: Color;
}
export const uselayoutStore = defineStore("layout", () => {

    const layouts = ref(layout);
    const boxlayout = ref<boolean>(true);
    const sidebar = ref<string>('default');
    const svg = ref<string>('stroke-svg')


    function setLayout(val: any) {


        if (val?.class == "dark-only") {
            document.body.classList.contains("light") && document.body.classList.remove("light");
        } else {
            document.body.classList.contains("dark-only") && document.body.classList.remove("dark-only");
        }
        document.body.classList.add(val?.class || "");
    }
    document.body.setAttribute("main-theme-layout", layouts.value.settings.layout_type);
    document.getElementsByTagName("html")[0].setAttribute("dir", layouts.value.settings.layout_type);
    var primaryColor: string = localStorage.getItem("primary_color") || layouts.value.color.primary_color;
    var secondaryColor = localStorage.getItem("secondary_color") || layouts.value.color.secondary_color;
    var layoutVersion = localStorage.getItem("layoutVersion") || layouts.value.color.layout_version;

    if (primaryColor || secondaryColor) {
        addStyle(primaryColor, secondaryColor);
        if (layoutVersion)
            document.body.className = layoutVersion;
    }
    function addStyle(primary: string, secondary: string) {
        document.documentElement.style.setProperty("--theme-deafult", primary);
        document.documentElement.style.setProperty("--theme-secondary", secondary);
    }
    function setLayoutType(layout: any, val: any) {

        document.body.classList.remove("rtl");
        document.body.classList.remove("ltr");
        document.body.classList.remove("boxed");
        document.documentElement.removeAttribute("dir");
        document.body.setAttribute("class", val);
        document.body.setAttribute("main-theme-layout", val);

        layout.settings.layout_type = val;
        document.getElementsByTagName('html')[0].setAttribute('dir', val);
    }

    function setCustomizeSidebarType(val: any) {
        sidebar.value = val.type;
        localStorage.setItem("SidebarType", val);

    }
    function setSvg(svgs: string) {
        svg.value = svgs
        layouts.value.settings.sidebar_icon = svgs
    }
    function setColorScheme(color: any) {
        setColor(color);

        primaryColor = color.primary;
        secondaryColor = color.secondary
        layouts.value.color.layout_version = "light";
        localStorage.setItem("layoutVersion", layouts.value.color.layout_version);
    }
    function setColor(color: any) {
        addStyle(color.primary, color.secondary);
        localStorage.setItem("primary_color", color.primary);
        localStorage.setItem("secondary_color", color.secondary);
        window.location.reload();
    }
    return {
        layouts,
        setLayout,
        setLayoutType,
        boxlayout,
        setCustomizeSidebarType,
        setSvg,
        svg,

        setColorScheme
    };
});
