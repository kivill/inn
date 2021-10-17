<template>
  <q-page class="q-pa-md">
    <div class="row justify-center q-pa-xl q-gutter-md">
      <div class="col-6">
        <q-input
          outlined
          v-model="fondName"
          label="Название фонда"
          lazy-rules
        />
      </div>
      <div class="col-1">
        <q-btn label="Добавить" color="primary" size="lg" />
      </div>
    </div>
    <div class="row justify-center q-pt-md">
      <div class="col-8">
        <q-table title="Фонды" :rows="rows" :columns="columns" row-key="name">
          <template v-slot:header="props">
            <q-tr :props="props">
              <q-th auto-width />
              <q-th v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.label }}
              </q-th>
            </q-tr>
          </template>

          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td auto-width>
                <q-btn
                  size="sm"
                  color="primary"
                  round
                  dense
                  @click="props.expand = !props.expand"
                  :icon="props.expand ? 'expand_more' : 'chevron_right'"
                />
              </q-td>
              <q-td v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.value }}
              </q-td>
            </q-tr>
            <q-tr v-show="props.expand" :props="props">
              <q-td colspan="100%">
                <div v-if="props.row.checkData.length == 0">
                  Данные еще собираются
                </div>
                <div v-else class="row q-gutter-md">
                  <div
                    v-for="(check, index) in props.row.checkData"
                    :key="index"
                    class="col-6"
                  >
                    <div v-if="check.type == 'okved'">
                      <div v-if="check.status">
                        <q-icon name="check_circle" color="green" size="sm" />
                        Оквед соответствует
                      </div>
                      <div v-if="!check.status">
                        <q-icon name="error_outline" color="red" size="sm" />
                        Оквед не соответствует
                      </div>
                    </div>
                    <div v-if="check.type == 'fondDobroMail'">
                      <div v-if="check.status">
                        <q-icon name="check_circle" color="green" size="sm" />
                        Зарегистрированы в Добро mail.ru
                      </div>
                      <div v-if="!check.status">
                        <q-icon name="error_outline" color="red" size="sm" />
                        Не зарегистрированы в Добро mail.ru
                      </div>
                    </div>
                    <div v-if="check.type == 'fondNeedsHelp'">
                      <div v-if="check.status">
                        <q-icon name="check_circle" color="green" size="sm" />
                        Зарегистрированы в Фонде «Нужна помощь»
                      </div>
                      <div v-if="!check.status">
                        <q-icon name="error_outline" color="red" size="sm" />
                        Не зарегистрированы в Фонде «Нужна помощь»
                      </div>
                    </div>
                    <div v-if="check.type == 'fondAllTogether'">
                      <div v-if="check.status">
                        <q-icon name="check_circle" color="green" size="sm" />
                        Зарегистрированы в Ассоциации НКО «Все вместе»
                      </div>
                      <div v-if="!check.status">
                        <q-icon name="error_outline" color="red" size="sm" />
                        Не зарегистрированы в Ассоциации НКО «Все вместе»
                      </div>
                    </div>
                  </div>
                </div>
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'PageIndex',
  setup() {
    const columns = [
      {
        name: 'name',
        field: 'name',
        label: 'Название фонда',
        align: 'left',
      },
      {
        name: 'score',
        field: 'score',
        label: 'Оценка',
        format: (val: string) => `${val}%`,
        align: 'left',
      },
      {
        name: 'status',
        field: 'status',
        label: 'Статус проверки',
        align: 'left',
      },
    ];
    const rows = [
      {
        name: 'Фонд ДЛОР',
        score: 0,
        status: 'created',
        checkData: [],
      },
      {
        name: 'Фонд ОРУГ',
        score: 100,
        status: 'done',
        checkData: [
          {
            type: 'okved',
            status: true,
          },
          {
            type: 'fondDobroMail',
            status: true,
          },
          {
            type: 'fondNeedsHelp',
            status: true,
          },
          {
            type: 'fondAllTogether',
            status: true,
          },
        ],
      },
      {
        name: 'Фонд ПРО',
        score: 0,
        status: 'done',
        checkData: [
          {
            type: 'okved',
            status: false,
          },
          {
            type: 'fondDobroMail',
            status: false,
          },
          {
            type: 'fondNeedsHelp',
            status: false,
          },
          {
            type: 'fondAllTogether',
            status: false,
          },
        ],
      },
    ];
    const fondName = ref('');
    return { columns, rows, fondName };
  },
});
</script>
