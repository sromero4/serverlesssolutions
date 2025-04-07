<template>
    <Card1 dropdown="true" headerTitle="true" title="Habitantes"
        cardhaderClass="card-no-border" cardbodyClass="pt-0 projects px-0">
        <ul class="pagination mx-2 mt-2 justify-content-end">
            <li class="page-item"><a class="page-link" @click="prev()">Anterior</a></li>
            <li class="page-item" v-for="i in num_pages()" :key="i" v-bind:class="[i == currentPage ? 'active' : '']"
                v-on:click="change_page(i)">
                <a class="page-link">{{ i }}</a>
            </li>
            <li class="page-item"><a class="page-link" @click="change()">Siguiente</a></li>
        </ul>
        <div class="table-responsive theme-scrollbar">
            <div id="recent-order_wrapper" class="dataTables_wrapper no-footer">
                <div id="recent-order_filter" class="dataTables_filter"><label>Buscar:<input type="search" placeholder=""
                            v-model="filterQuery"></label></div>
                <table class="table display dataTable no-footer" id="information" style="width:100%">
                    <thead>
                        <tr>
                            <th>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="">
                                    <label class="form-check-label"></label>
                                </div>
                            </th>
                            <th>Torre y apto </th>
                            <th>Nombre Propietario</th>
                            <th>Contacto</th>
                            <th>Placa</th>
                        </tr>
                    </thead>
                    <tbody v-if="!get_rows().length">
                        <tr class="odd">
                            <td valign="top" colspan="6" class="dataTables_empty">No se encuentran datos</td>
                        </tr>
                    </tbody>
                    <tbody v-if="get_rows().length">
                        <tr v-for="(row, index) in get_rows()" :key="index">
                            <td>
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" value="">
                                    <label class="form-check-label"></label>
                                </div>
                            </td>
                            <td>
                                <div class="d-flex align-items-center">
                                    <h6>{{ row.apto }}</h6>
                                </div>
                            </td>
                            <td class="project-dot">
                                <div class="d-flex">
                                    <div class="flex-shrink-0"><span :class="row.bgclass"></span></div>
                                    <div class="flex-grow-1">
                                        <h6>{{ row.nombre_propietario }}</h6>
                                    </div>
                                </div>
                            </td>
                            <td> {{ row.contacto }}</td>
                            <td>{{ row.placa }}</td>
                        </tr>
                    </tbody>
                </table>

            </div>
        </div>
    </Card1>
</template>
<script lang="ts" setup>
import { ref, defineAsyncComponent, onMounted, watch } from 'vue'
import { project, napoli } from "@/core/data/dashboards"
import { getImages } from "@/composables/common/getImages"
const Card1 = defineAsyncComponent(() => import("@/components/common/card/CardData1.vue"))
let elementsPerPage = ref<number>(20)
let currentPage = ref<number>(1)
let filterQuery = ref<string>("")
let allData = ref<any>([])
watch(filterQuery, (search: string) => {

    var filteredData = napoli.filter((row) => {
        return (
            row.nombre_propietario.toLowerCase().includes(search.toLowerCase()) ||
            row.apto.toLowerCase().includes(search.toLowerCase()) ||
            row.placa.toLowerCase().includes(search.toLowerCase())
        );
    });
    search == "" ? allData.value = napoli : allData.value = filteredData
})
function get_rows() {
    var start = (currentPage.value - 1) * elementsPerPage.value;
    var end = start + elementsPerPage.value;
    return allData.value.slice(start, end);
}
function num_pages() {
    return Math.ceil(allData.value.length / elementsPerPage.value);
}
function change_page(page: number) {
    currentPage.value = page;
}
function change() {
    if (currentPage.value < Math.ceil(allData.value.length / elementsPerPage.value)) {
        currentPage.value++;
    }
}
function prev() {
    if (currentPage.value > 1) {
        currentPage.value--;
    }
}

onMounted(() => {
    allData.value = napoli;
})
</script>