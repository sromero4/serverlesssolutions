<template>
	<div id="sc-page-wrapper">
		<div id="sc-page-content">
			<div class="uk-flex uk-flex-center">
				<div class="uk-grid" data-uk-grid>
					<div class="uk-width-1-4@m uk-width-1-5@l">
						<div v-sc-sticky="sideMenu">
							<ul class="uk-subnav uk-subnav-pill uk-flex-column" data-uk-switcher="connect: .sc-settings-container; animation: uk-animation-slide-bottom-small; swiping: false" style="align-items:normal;">
								<li class="uk-active">
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-cogs uk-margin-medium-right"></i>{{ $t('Basic data') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-cogs uk-margin-medium-right"></i>{{ $t('Optional Data') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-account-key-outline uk-margin-medium-right"></i>{{ $t('Assigned modules') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-account-key-outline uk-margin-medium-right"></i>{{ $t('Module permissions') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-account-cog-outline uk-margin-medium-right"></i>{{ $t('Staff to assign') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-folder-alert-outline uk-margin-medium-right"></i>{{ $t('Restrictions') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-cube-scan uk-margin-medium-right"></i>{{ $t('Type') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-cellphone uk-margin-medium-right"></i>{{ $t('Mobile app') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-diving-scuba-flag uk-margin-medium-right"></i>{{ $t('Divisions') }}
										</span>
									</a>
								</li>
								<li>
									<a href="javascript:void(0)">
										<span class="uk-flex uk-flex-middle uk-text-medium sc-text-semibold">
											<i class="mdi mdi-diving-scuba-flag uk-margin-medium-right"></i>{{ $t('General Information') }}
										</span>
									</a>
								</li>
							</ul>
						</div>
					</div>
					<div class="uk-width-3-4@m">
						<form ref="createUsers" action="">
							<ul class="uk-switcher sc-settings-container">
								<!--BASIC DATA-->
								<li>
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													{{ $t('Basic data') }}
												</ScCardTitle>
												<ScCardMeta>
													{{ $t('Form to fill in the basic data necessary for the creation of a user.') }}
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event, 'CREATE')">
													{{ $t('Save') }}
												</button>
											</div>
											
											<div v-if="infoloading">
												<ScProgressCircular size="lg"></ScProgressCircular>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-3@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--Login Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Login') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<ScInput id="settings-basic-usuarioLogin" 
																	v-model="$v.usuarioLogin.$model" 
																	name="usuarioLogin" 
																	:error-state="$v.usuarioLogin.$error" 
																	:validator="$v.usuarioLogin"
																>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.usuarioLogin.required">
																		Field is required
																	</li>
																</ul>
															</div>
															<!--Name Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Name') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<ScInput id="settings-basic-name" 
																	v-model="$v.name.$model"
																	name="name" 
																	:error-state="$v.name.$error" 
																	:validator="$v.name"
																>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.name.required">
																		Field is required
																	</li>
																</ul>
															</div>
															<!--Password Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Password') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<ScInput id="settings-basic-clave" 
																	v-model="$v.password.$model" 
																	name="password" 
																	type="password" 
																	:error-state="$v.password.$error" 
																	:validator="$v.password"
																>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.password.required">
																		Password is required.
																	</li>
																	<li v-if="!$v.password.minLength">
																		Password must have at least {{ $v.password.$params.minLength.min }} characters.
																	</li>
																</ul>
															</div>
															<!--Repeat Password Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Repeat Password') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<ScInput id="settings-basic-repclave" 
																	v-model="$v.repeatPassword.$model" 
																	name="repeatPassword" 
																	type="password" 
																	:error-state="$v.repeatPassword.$error" 
																	:validator="$v.repeatPassword"
																>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.repeatPassword.sameAsPassword">
																		Passwords must be identical.
																	</li>
																</ul>
															</div>
															<!--City Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('City') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-ciudad"
																		v-model="$v.ciudad.$model"
																		:options="basicCiudad" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione la ciudad...', 'allowClear': true }"
																		:error-state="$v.ciudad.$error" 
																		:validator="$v.ciudad"
																	></Select2>
																	<ul class="sc-vue-errors">
																		<li v-if="!$v.ciudad.required">
																			Field is required
																		</li>
																	</ul>
																</client-only>
															</div>
															<!--Cedula Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Identification Card') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<ScInput id="settings-basic-cedula" 
																	v-model="$v.cedula.$model"
																	name="usuarioCedula"
																	type="number"
																	:error-state="$v.cedula.$error" 
																	:validator="$v.cedula"
																>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.cedula.required">
																		Field is required
																	</li>
																	<li v-if="!$v.cedula.maxLength">
																		The field must have a maximum of 10 characters.
																	</li>
																	<li v-if="!$v.cedula.minLength">
																		Cedula must have at least 7 characters.
																	</li>
																</ul>
															</div>
															<!--ESTADO Required	-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('State') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-estado"
																		v-model="$v.estado.$model"
																		:options="basicEstado"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el estado...', 'minimumResultsForSearch': -1, 'allowClear': true }"
																		:error-state="$v.estado.$error" 
																		:validator="$v.estado"
																	></Select2>
																	<ul class="sc-vue-errors">
																		<li v-if="!$v.estado.required">
																			Field is required
																		</li>
																	</ul>
																</client-only>
															</div>
															<!--Autoriza Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Authorize') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-autorizacion"
																		v-model="$v.autoriza.$model"
																		:options="basicAutorizacion"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione la autorizacion...', 'minimumResultsForSearch': -1, 'allowClear': true }"
																		:error-state="$v.autoriza.$error" 
																		:validator="$v.autoriza"
																	></Select2>
																	<ul class="sc-vue-errors">
																		<li v-if="!$v.autoriza.required">
																			Field is required
																		</li>
																	</ul>
																</client-only>
															</div>
															<!--Email-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Email') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<ScInput id="settings-page-email" 
																	v-model="$v.email.$model" 
																	v-input-mask="{ 'alias': 'email' }"
																	name="email" 
																	:error-state="$v.email.$error" 
																	:validator="$v.email"
																>
																</ScInput>
																<ul class="sc-vue-errors">
																	<li v-if="!$v.autoriza.required">
																		Field is required
																	</li>
																</ul>
															</div>
														</div>
													</div>
												</div>
											</div>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-2@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--CENTRO DE COSTO Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Centers of costs') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-centerCost"
																		v-model="$v.centroCosto.$model"
																		:options="basicCentroCosto"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione los centros de costos...' }"
																		multiple
																		:error-state="$v.centroCosto.$error" 
																		:validator="$v.centroCosto"
																	></Select2>
																	<ul class="sc-vue-errors">
																		<li v-if="!$v.centroCosto.required">
																			Field is required
																		</li>
																	</ul>
																</client-only>
															</div>
															<!--GRUPOS Required-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Groups') }} <span class="sc-color-label md-bg-red-400"></span>
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-grupo"
																		v-model="$v.grupo.$model"
																		:options="basicGrupo"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione los grupos...' }"
																		multiple
																		:error-state="$v.grupo.$error" 
																		:validator="$v.grupo"
																	></Select2>
																	<ul class="sc-vue-errors">
																		<li v-if="!$v.grupo.required">
																			Field is required
																		</li>
																	</ul>
																</client-only>
															</div>
														</div>
													</div>
												</div>
											</div>
											<!--div class="uk-margin-top">
												<div class="uk-grid-small uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-margin-small-top uk-display-inline-block" for="settings-page-notes">
															{{ $t('Please specify the reason for the update') }}: <span class="sc-color-label md-bg-red-400"></span>
														</label>
													</div>
													<div class="uk-width-expand">
														<ScTextarea id="settings-page-notes" 
															v-model="$v.notes.$model" 
															name ="notes" 
															:cols="20" 
															:rows="4" 
															:error-state="$v.notes.$error" 
															:validator="$v.notes">
														</ScTextarea>
														<ul class="sc-vue-errors">
															<li v-if="!$v.notes.required">
																Field is required
															</li>
														</ul>
													</div>
												</div>
											</div-->
										</ScCardBody>
									</ScCard>
								</li>
								<!--OPTIONAL DATA-->
								<li>
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													{{ $t('Optional data') }}
												</ScCardTitle>
												<ScCardMeta>
													{{ $t('Form to fill in the basic data necessary for the creation of a user.') }}
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'CREATE')">
													{{ $t('Save') }}
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-3@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--Cargo-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Burden') }}
																</label>
																<ScInput id="settings-basic-cargo" 
																	v-model="settings.basic.cargo"
																	name="usuarioCargo"
																>
																</ScInput>
															</div>
															<!--AREA-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Area') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-area"
																		v-model="settings.basic.area"
																		:options="basicArea"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el area...', 'minimumResultsForSearch': -1, 'allowClear': true }"
																	></Select2>
																</client-only>
															</div>
															<!--CENTRO CAJA-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Center Box') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-centro-caja"
																		v-model="settings.basic.centroCaja"
																		:options="basicCentroCaja"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el centro...', 'allowClear': true }"
																	></Select2>
																</client-only>
															</div>
															<!--Proceso-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Process') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-proceso"
																		v-model="settings.basic.proceso"
																		:options="basicProceso" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el proceso...', allowClear: true }"
																	></Select2>
																	<p class="uk-text-large uk-margin-medium-bottom">
																		Prompt
																	</p>
																	<a class="sc-button" href="javascript:void(0)" @click="openDialog('prompt')">
																		Open
																	</a>
																	<div class="uk-margin-small-top">
																		<span class="uk-text-muted">Your Name:</span> {{ promptName }}
																	</div>
																</client-only>
															</div>
															<!--Comercial-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Commercial') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-comercial"
																		v-model="settings.basic.comercial"
																		:options="basicComercial" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el comercial...', allowClear: true }"
																	></Select2>
																</client-only>
															</div>
															<!--Cliente-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Client') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-cliente"
																		v-model="settings.basic.cliente"
																		:options="basicCliente" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el cliente...', allowClear: true }"
																	></Select2>
																</client-only>
															</div>
															<!--Tercero-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Third') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-tercero"
																		v-model="settings.basic.tercero"
																		:options="basicTercero" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el tercero...', allowClear: true }"
																	></Select2>
																</client-only>
															</div>
															<!--Ingreso Certificado-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Certified Income') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-ingresoCertificado"
																		v-model="settings.basic.ingresoCertificado"
																		:options="basicIngresoCertificado" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el ingreso del certificado...', 'minimumResultsForSearch': -1, allowClear: true }"
																	></Select2>
																</client-only>
															</div>
														</div>
													</div>
												</div>
											</div>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-2@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Cellar') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-bodega"
																		v-model="settings.basic.bodega"
																		:options="basicBodega"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione las bodegas...' }"
																		multiple
																	></Select2>
																</client-only>
															</div>
														</div>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--MODULOS ASIGNADOS-->
								<li> 
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													Users
												</ScCardTitle>
												<ScCardMeta>
													Lorem ipsum dolor, sit amet consectetur adipisicing elit. Unde, nulla.
												</ScCardMeta>
											</div>
											<div>
												<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-trash-can-outline sc-icon-square sc-light"></a>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-overflow-auto">
												<table class="uk-table uk-table-divider">
													<thead>
														<tr>
															<th>
																<div class="uk-flex">
																	<PrettyCheck v-model="userTable.checkAll"
																		class="p-icon"
																		:indeterminate.sync="userTable.checkAllInd"
																		@change="toggleAllUsers($event)"
																	>
																		<i slot="extra" class="icon mdi mdi-check"></i>
																		<i slot="indeterminate-extra" class="icon mdi mdi-minus"></i>
																		<label slot="indeterminate-label"></label>
																	</PrettyCheck>
																</div>
															</th>
															<th>User Name</th>
															<th>Email</th>
															<th>Phone Number</th>
															<th>Status</th>
															<th>Actions</th>
														</tr>
													</thead>
													<tbody>
														<tr v-for="user in settings.users" :key="user.id" class="uk-table-middle">
															<td class="uk-table-shrink">
																<div class="uk-flex">
																	<PrettyCheck v-model="user.selected" class="p-icon" @change="toggleUser($event)">
																		<i slot="extra" class="icon mdi mdi-check"></i>
																	</PrettyCheck>
																</div>
															</td>
															<td class="sc-text-semibold uk-text-nowrap">
																{{ user.fName }} {{ user.lName }}
															</td>
															<td>{{ user.email }}</td>
															<td class="uk-text-nowrap">
																{{ user.phone }}
															</td>
															<td class="uk-table-shrink">
																<span v-if="user.status === 'active'" class="uk-label uk-label-success">
																	{{ user.status }}
																</span>
																<span v-if="user.status === 'disabled'" class="uk-label uk-label-danger">
																	{{ user.status }}
																</span>
															</td>
															<td class="uk-text-nowrap uk-table-shrink">
																<a href="javascript:void(0)" class="mdi mdi-pencil sc-icon-square"></a>
																<a href="javascript:void(0)" class="mdi mdi-trash-can-outline sc-icon-square"></a>
															</td>
														</tr>
													</tbody>
												</table>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--PERMISOS DEL MODULO-->
								<li> 
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													Appearance
												</ScCardTitle>
												<ScCardMeta>
													Lorem ipsum dolor, sit amet consectetur adipisicing elit. Unde, nulla.
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button">
													Save
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div>
												<div class="uk-flex-middle uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary" for="settings-page-appearance-scheme">
															Color Scheme
														</label>
													</div>
													<div class="uk-width-1-4@l uk-width-1-2@m">
														<client-only>
															<Select2
																id="settings-page-appearance-scheme"
																v-model="settings.apperance.colorScheme"
																:options="apperanceScheme"
																:settings="{ 'width': '100%', 'placeholder': 'Select color scheme...', 'minimumResultsForSearch': -1, 'allowClear': true }"
															></Select2>
														</client-only>
													</div>
												</div>
											</div>
											<div class="uk-margin">
												<div class="uk-flex-middle uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary" for="settings-page-appearance-layout">
															Layout
														</label>
													</div>
													<div class="uk-width-1-4@l uk-width-1-2@m">
														<client-only>
															<Select2
																id="settings-page-appearance-layout"
																v-model="settings.apperance.layout"
																:options="apperanceLayout"
																:settings="{ 'width': '100%', 'placeholder': 'Select layout...', 'minimumResultsForSearch': -1, 'allowClear': true }"
															></Select2>
														</client-only>
													</div>
												</div>
											</div>
											<div class="uk-margin-medium">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Sticky Header
														</label>
													</div>
													<div class="uk-width-expand@m">
														<span class="uk-margin-right">
															<PrettyRadio v-model="settings.apperance.stickyHeader" value="yes" class="p-radio" name="sticky-header">
																Yes
															</PrettyRadio>
														</span>
														<span>
															<PrettyRadio v-model="settings.apperance.stickyHeader" value="no" class="p-radio" name="sticky-header">
																No
															</PrettyRadio>
														</span>
													</div>
												</div>
											</div>
											<div class="uk-margin-medium">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block" for="settings-page-appearance-fonts">
															Global Font
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<Select2
																id="settings-page-appearance-fonts"
																v-model="settings.apperance.fontFamily"
																:options="apperanceFonts"
																:settings="{ 'width': '100%', 'placeholder': 'Select font family...', 'minimumResultsForSearch': -1, 'allowClear': true }"
															></Select2>
														</client-only>
													</div>
												</div>
											</div>
											<h5 class="uk-heading-line uk-margin-large-top">
												<span>Colors</span>
											</h5>
											<div>
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Primary
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<ScColorpicker v-model="settings.apperance.colorPrimary"
																size="large"
															></ScColorpicker>
														</client-only>
														<span class="uk-form-help-block uk-margin-remove-left uk-margin-mini-top">
															Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fuga, ullam.
														</span>
													</div>
												</div>
											</div>
											<div class="uk-margin-top">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Secondary
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<ScColorpicker v-model="settings.apperance.colorSecondary"
																size="large"
															></ScColorpicker>
														</client-only>
														<span class="uk-form-help-block uk-margin-remove-left uk-margin-mini-top">
															Lorem ipsum dolor sit amet, ullam.
														</span>
													</div>
												</div>
											</div>
											<div class="uk-margin-top">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Links
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<ScColorpicker v-model="settings.apperance.colorLinks"
																size="large"
																:pallete="['#5e35b1', '#689f38', '#1e88e5', '#e53935']"
															></ScColorpicker>
														</client-only>
														<span class="uk-form-help-block uk-margin-remove-left uk-margin-mini-top">
															Lorem ipsum dolor sit amet.
														</span>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--PERSONAL PARA ASIGNAR-->
								<li> 
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													Plugins
												</ScCardTitle>
												<ScCardMeta>
													Lorem ipsum dolor, sit amet consectetur adipisicing elit. Unde, nulla.
												</ScCardMeta>
											</div>
											<div>
												<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-trash-can-outline sc-icon-square sc-light"></a>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-overflow-auto">
												<table class="uk-table uk-table-divider">
													<thead>
														<tr>
															<th>
																<div class="uk-flex">
																	<PrettyCheck v-model="pluginTable.checkAll"
																		class="p-icon"
																		:indeterminate.sync="pluginTable.checkAllInd"
																		@change="toggleAllPlugins($event)"
																	>
																		<i slot="extra" class="icon mdi mdi-check"></i>
																		<i slot="indeterminate-extra" class="icon mdi mdi-minus"></i>
																		<label slot="indeterminate-label"></label>
																	</PrettyCheck>
																</div>
															</th>
															<th>Name</th>
															<th>Version</th>
															<th>Description</th>
															<th>Status</th>
															<th>Actions</th>
														</tr>
													</thead>
													<tbody>
														<tr v-for="plugin in settings.plugins" :key="plugin.id" class="uk-table-middle">
															<td class="uk-table-shrink">
																<div class="uk-flex">
																	<PrettyCheck v-model="plugin.selected" class="p-icon" @change="togglePlugin($event)">
																		<i slot="extra" class="icon mdi mdi-check"></i>
																	</PrettyCheck>
																</div>
															</td>
															<td class="sc-text-semibold uk-text-nowrap">
																{{ plugin.name }}
															</td>
															<td class="uk-text-nowrap uk-table-shrink">
																{{ plugin.version }}
															</td>
															<td class="uk-text-nowrap">
																{{ plugin.description }}
															</td>
															<td class="uk-table-shrink">
																<span v-if="plugin.status === 'active'" class="uk-label uk-label-success">
																	{{ plugin.status }}
																</span>
																<span v-if="plugin.status === 'disabled'" class="uk-label md-bg-grey-500">
																	{{ plugin.status }}
																</span>
															</td>
															<td class="uk-text-nowrap uk-table-shrink">
																<a href="javascript:void(0)"
																	class="mdi sc-icon-square"
																	:data-uk-tooltip="plugin.status === 'active' ? 'Deactivate' : 'Activate'"
																	:class="{ 'md-color-green-600' : plugin.status === 'active', 'mdi-toggle-switch': plugin.status === 'active', 'mdi-toggle-switch-off': plugin.status === 'disabled' }"
																	@click.prevent="togglePluginStatus(plugin)"
																></a>
																<a href="javascript:void(0)" class="mdi mdi-trash-can-outline sc-icon-square"></a>
															</td>
														</tr>
													</tbody>
												</table>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--RESTRICCIONES-->
								<li>
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													{{ $t('Basic data') }}
												</ScCardTitle>
												<ScCardMeta>
													{{ $t('Form to fill in the basic data necessary for the creation of a user.') }}
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'CREATE')">
													{{ $t('Save') }}
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-3@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--Restriccion Horario-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Time Restriction') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-restriccionHorario"
																		v-model="settings.basic.restriccionHorario"
																		:options="basicRestriccionHorario" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione la restricción de horario...', 'minimumResultsForSearch': -1, allowClear: true }"
																	></Select2>
																</client-only>
															</div>
															<!--Restriccion IP-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('IP restriction') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-restriccionIP"
																		v-model="settings.basic.restriccionIP"
																		:options="basicRestriccionIP" 
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione la restricción de la IP...', 'minimumResultsForSearch': -1, allowClear: true }"
																	></Select2>
																</client-only>
															</div>
															<!--Tiempo Caducidad-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Expiration Time') }} ({{ $t('Minutes') }})
																</label>
																<ScInput id="settings-basic-tiempoCaducidad" v-model="settings.basic.tiempoCaducidad"></ScInput>
															</div>
														</div>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--TIPO -->
								<li> 
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													Users
												</ScCardTitle>
												<ScCardMeta>
													Lorem ipsum dolor, sit amet consectetur adipisicing elit. Unde, nulla.
												</ScCardMeta>
											</div>
											<div>
												<a href="javascript:void(0)" class="sc-actions-icon mdi mdi-trash-can-outline sc-icon-square sc-light"></a>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-overflow-auto">
												<table class="uk-table uk-table-divider">
													<thead>
														<tr>
															<th>
																<div class="uk-flex">
																	<PrettyCheck v-model="userTable.checkAll"
																		class="p-icon"
																		:indeterminate.sync="userTable.checkAllInd"
																		@change="toggleAllUsers($event)"
																	>
																		<i slot="extra" class="icon mdi mdi-check"></i>
																		<i slot="indeterminate-extra" class="icon mdi mdi-minus"></i>
																		<label slot="indeterminate-label"></label>
																	</PrettyCheck>
																</div>
															</th>
															<th>User Name</th>
															<th>Email</th>
															<th>Phone Number</th>
															<th>Status</th>
															<th>Actions</th>
														</tr>
													</thead>
													<tbody>
														<tr v-for="user in settings.users" :key="user.id" class="uk-table-middle">
															<td class="uk-table-shrink">
																<div class="uk-flex">
																	<PrettyCheck v-model="user.selected" class="p-icon" @change="toggleUser($event)">
																		<i slot="extra" class="icon mdi mdi-check"></i>
																	</PrettyCheck>
																</div>
															</td>
															<td class="sc-text-semibold uk-text-nowrap">
																{{ user.fName }} {{ user.lName }}
															</td>
															<td>{{ user.email }}</td>
															<td class="uk-text-nowrap">
																{{ user.phone }}
															</td>
															<td class="uk-table-shrink">
																<span v-if="user.status === 'active'" class="uk-label uk-label-success">
																	{{ user.status }}
																</span>
																<span v-if="user.status === 'disabled'" class="uk-label uk-label-danger">
																	{{ user.status }}
																</span>
															</td>
															<td class="uk-text-nowrap uk-table-shrink">
																<a href="javascript:void(0)" class="mdi mdi-pencil sc-icon-square"></a>
																<a href="javascript:void(0)" class="mdi mdi-trash-can-outline sc-icon-square"></a>
															</td>
														</tr>
													</tbody>
												</table>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--APLICACIONES MOVILES-->
								<li>
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													{{ $t('Mobile app') }}
												</ScCardTitle>
												<ScCardMeta>
													{{ $t('Form to fill in the basic data necessary for the creation of a user.') }}
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'CREATE')">
													{{ $t('Save') }}
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-2@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--Tipo Usuario APP-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('App User Type') }}
																</label>
																<client-only>
																	<Select2
																		id="settings-basic-tipoUsuario"
																		v-model="settings.basic.tipoUsuario"
																		:options="basicTipoUsuario"
																		:settings="{ 'width': '100%', 'placeholder': 'Seleccione el tipo de usuario...', 'minimumResultsForSearch': -1, 'allowClear': true }"
																	></Select2>
																</client-only>
															</div>
														</div>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<li> 
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													Appearance
												</ScCardTitle>
												<ScCardMeta>
													Lorem ipsum dolor, sit amet consectetur adipisicing elit. Unde, nulla.
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button">
													Save
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div>
												<div class="uk-flex-middle uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary" for="settings-page-appearance-scheme">
															Color Scheme
														</label>
													</div>
													<div class="uk-width-1-4@l uk-width-1-2@m">
														<client-only>
															<Select2
																id="settings-page-appearance-scheme"
																v-model="settings.apperance.colorScheme"
																:options="apperanceScheme"
																:settings="{ 'width': '100%', 'placeholder': 'Select color scheme...', 'minimumResultsForSearch': -1, 'allowClear': true }"
															></Select2>
														</client-only>
													</div>
												</div>
											</div>
											<div class="uk-margin">
												<div class="uk-flex-middle uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary" for="settings-page-appearance-layout">
															Layout
														</label>
													</div>
													<div class="uk-width-1-4@l uk-width-1-2@m">
														<client-only>
															<Select2
																id="settings-page-appearance-layout"
																v-model="settings.apperance.layout"
																:options="apperanceLayout"
																:settings="{ 'width': '100%', 'placeholder': 'Select layout...', 'minimumResultsForSearch': -1, 'allowClear': true }"
															></Select2>
														</client-only>
													</div>
												</div>
											</div>
											<div class="uk-margin-medium">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Sticky Header
														</label>
													</div>
													<div class="uk-width-expand@m">
														<span class="uk-margin-right">
															<PrettyRadio v-model="settings.apperance.stickyHeader" value="yes" class="p-radio" name="sticky-header">
																Yes
															</PrettyRadio>
														</span>
														<span>
															<PrettyRadio v-model="settings.apperance.stickyHeader" value="no" class="p-radio" name="sticky-header">
																No
															</PrettyRadio>
														</span>
													</div>
												</div>
											</div>
											<div class="uk-margin-medium">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block" for="settings-page-appearance-fonts">
															Global Font
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<Select2
																id="settings-page-appearance-fonts"
																v-model="settings.apperance.fontFamily"
																:options="apperanceFonts"
																:settings="{ 'width': '100%', 'placeholder': 'Select font family...', 'minimumResultsForSearch': -1, 'allowClear': true }"
															></Select2>
														</client-only>
													</div>
												</div>
											</div>
											<h5 class="uk-heading-line uk-margin-large-top">
												<span>Colors</span>
											</h5>
											<div>
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Primary
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<ScColorpicker v-model="settings.apperance.colorPrimary"
																size="large"
															></ScColorpicker>
														</client-only>
														<span class="uk-form-help-block uk-margin-remove-left uk-margin-mini-top">
															Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fuga, ullam.
														</span>
													</div>
												</div>
											</div>
											<div class="uk-margin-top">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Secondary
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<ScColorpicker v-model="settings.apperance.colorSecondary"
																size="large"
															></ScColorpicker>
														</client-only>
														<span class="uk-form-help-block uk-margin-remove-left uk-margin-mini-top">
															Lorem ipsum dolor sit amet, ullam.
														</span>
													</div>
												</div>
											</div>
											<div class="uk-margin-top">
												<div class="uk-grid" data-uk-grid>
													<div class="uk-width-1-4@m">
														<label class="sc-color-secondary uk-display-inline-block">
															Links
														</label>
													</div>
													<div class="uk-width-1-2@m">
														<client-only>
															<ScColorpicker v-model="settings.apperance.colorLinks"
																size="large"
																:pallete="['#5e35b1', '#689f38', '#1e88e5', '#e53935']"
															></ScColorpicker>
														</client-only>
														<span class="uk-form-help-block uk-margin-remove-left uk-margin-mini-top">
															Lorem ipsum dolor sit amet.
														</span>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--DIVISIONES-->
								<li>
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													{{ $t('Basic data') }}
												</ScCardTitle>
												<ScCardMeta>
													{{ $t('Form to fill in the basic data necessary for the creation of a user.') }}
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'CREATE')">
													{{ $t('Save') }}
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-2@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--Fecha Cambio Clave-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Key Change Date') }}
																</label>
																<ScInput id="settings-basic-fechaCambioClave" v-model="settings.basic.fechaCambioClave"></ScInput>
															</div>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('User') }}
																</label>
																Usuario Creador
															</div>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Date created') }}
																</label>
															</div>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Date modified') }}
																</label>
															</div>
														</div>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
								<!--GENERAL INFORMATION-->
								<li>
									<ScCard>
										<ScCardHeader class="uk-flex uk-flex-middle sc-theme-bg-dark sc-light" separator>
											<div class="uk-flex-1">
												<ScCardTitle>
													{{ $t('Basic data') }}
												</ScCardTitle>
												<ScCardMeta>
													{{ $t('Form to fill in the basic data necessary for the creation of a user.') }}
												</ScCardMeta>
											</div>
											<div>
												<button class="sc-button sc-button-success" :disabled="submitStatus === 'PENDING'" @click="submitForm($event,'CREATE')">
													{{ $t('Save') }}
												</button>
											</div>
										</ScCardHeader>
										<ScCardBody>
											<div class="uk-margin-top">
												<div class="uk-flex-middle uk-grid uk-grid-match" data-uk-grid>
													<div class="uk-width-expand@m">
														<div class="uk-child-width-1-2@m uk-flex uk-flex-bottom uk-grid" data-uk-grid>
															<!--Fecha Cambio Clave-->
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Key Change Date') }}
																</label>
																<ScInput id="settings-basic-fechaCambioClave" v-model="settings.basic.fechaCambioClave"></ScInput>
															</div>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('User') }}
																</label>
																Usuario Creador
															</div>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Date created') }}
																</label>
															</div>
															<div>
																<label class="sc-color-secondary" for="settings-page-title">
																	{{ $t('Date modified') }}
																</label>
															</div>
														</div>
													</div>
												</div>
											</div>
										</ScCardBody>
									</ScCard>
								</li>
							</ul>
						</form>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import { scHelpers, scFakeData } from "~/assets/js/utils";
const { uniqueID } = scHelpers;
const { first, last, phone, email, sentence, floating, name, city} = scFakeData;

const countries = require('~/data/common/countries.json');

import ScInput from '~/components/Input'
import 'vue-good-table/dist/vue-good-table.css'
import { VueGoodTable } from 'vue-good-table';
//import ScTextarea from '~/components/Textarea'
import PrettyCheck from 'pretty-checkbox-vue/check'
import PrettyRadio from 'pretty-checkbox-vue/radio'
import ScColorpicker from '~/components/Colorpicker'
import { provideApolloClient, useMutation, useQuery } from '@vue/apollo-composable';
import gql from 'graphql-tag'
import { required, minLength, sameAs, maxLength } from 'vuelidate/lib/validators'

import customValidators from '~/plugins/vuelidateValidators'

import sticky from '~/plugins/stickyKit'

require('~/assets/icons/flags/flags.css');
require('~/plugins/jquery');
if(process.client) {
	require('~/assets/js/vendor/jquery.quicksearch.js');
}

import { validationMixin } from 'vuelidate'
import moment from 'moment'
import { logErrorMessages } from '@vue/apollo-util'
import { watch } from 'vue'
import { ScProgressCircular } from '~/components/progress'

if(process.client) {
	require('~/plugins/inputmask')
}

export default {
	name: 'HomeUsuario',
	components: {
		Select2: process.client ? () => import('~/components/Select2') : null,
		//MultiSelect: process.client ? () => import('~/components/Multiselect') : null,
		ScInput,
		//ScTextarea,
		PrettyCheck,
		PrettyRadio,
		ScColorpicker,
		ScProgressCircular
	},
	mixins: [validationMixin],
	apollo: {
	},
	data: () => ({
		filter: {
			codigo: '',
			usuarioLogin: '',
			nombre: '',
			ciudad: '',
			cedula: '',
			estado: '',
			email: '',
			cliente: '',
			tercero: '',
			fecha: '',
					
		},
		status: {
			type: '',
			message:''
		},
		submitStatus: null,
		loading:null,
		invalid:false,
		promptName: '',
		max: 10,
		usuarioLogin: '',
		name: '',
		password: '',
		repeatPassword: '',
		notes: '',
		cedula: '',
		ciudad: '',
		estado: '',
		autoriza: '',
		centroCosto: '',
		grupo: '',
		email: '',
		settings: { //Datos por defecto de las secciones
			basic: { 
				pageOnline: true,
				pageTitle: 'Creacion de Usuarios',
				pageKeywords: [1, 2],
				accessAllow: ['US', 'CN', 'BR', 'PL', 'ES', 'IN'],
				centroCosto: [],
				grupo: [],
				bodega: [],
				SSL: '',
				ciudad: ['US'],
				estado: [],
				centroCaja: [],
				area: [],
				autorizacion: [],
				proceso: [],
				comercial: [],
				cliente: [], 
				tercero: [],
				ingresoCertificado: [],
				restriccionHorario: [],
				restriccionIP: [],
				tipoUsuario: [],
				searchable: '',
			},
			users: [],
			apperance: {
				colorScheme: '',
				layout: '',
				stickyHeader: 'no',
				fontFamily: '',
				colorPrimary: '',
				colorSecondary: '',
				colorLinks: '#1e88e5'
			},
			plugins: [],
		},
		keywords: [
			{ id: 1, text: 'Admin template' },
			{ id: 2, text: 'UIkit' },
			{ id: 3, text: 'Multipurpose' },
			{ id: 4, text: 'VueJS' }
		],
		userTable: {
			checkAll: false,
			checkAllInd: false
		},
		pluginTable: {
			checkAll: false,
			checkAllInd: false
		},
		apperanceScheme: [
			{ id: 1, text: 'Light' },
			{ id: 2, text: 'Dark' },
		],
		apperanceLayout: [
			{ id: 1, text: 'Default' },
			{ id: 2, text: 'Blog' },
			{ id: 2, text: 'Portfolio' }
		],
		apperanceFonts: [
			{ id: 1, text: 'Roboto, sans-serif' },
			{ id: 2, text: 'Helvetica, sans-serif' },
			{ id: 3, text: 'Trebuchet MS, sans-serif' },
			{ id: 4, text: 'Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif' }
		],
		basicCiudad: [{ id: 1, text: 'Roboto, sans-serif' }],
		basicEstado: [], //READY
		basicCentroCaja: [], //READY
		basicArea: [], //READY
		basicAutorizacion: [ //READY
			{ id: 'SI', text: 'SI' },
			{ id: 'NO', text: 'NO'}
		],
		basicProceso: [],
		basicComercial: [],
		basicCliente: [], //READY
		basicTercero: [],
		basicIngresoCertificado: [ //READY
			{ id: 'SI', text: 'SI' },
			{ id: 'NO', text: 'NO'}
		],
		basicRestriccionHorario: [ //READY
			{ id: 'SI', text: 'SI' },
			{ id: 'NO', text: 'NO'}
		],
		basicRestriccionIP: [ //READY
			{ id: 'SI', text: 'SI' },
			{ id: 'NO', text: 'NO'}
		],
		basicTipoUsuario: [ //READY
			{ id: 'NORMAL', text: 'NORMAL' },
			{ id: 'ADMIN', text: 'ADMIN'}
		],
		basicCentroCosto: [], //READY
		basicGrupo: [], //READY
		basicBodega: [], //READY
		sideMenu: {
			media: 'mediumMin',
			options: {
				'offset_top': 'inPlace'
			},
			on: {
				'sticky_kit:stick' (e) {
					// console.log("has stuck!", e.target);
				},
				'sticky_kit:unstick' (e) {
					// console.log("has unstuck!", e.target);
				},
			}
		},
	}),
	computed: {
		infoloading () {
			if (this.loading)
				if(this.loading.value){
					return this.loading.value
				}
			return false
		},
		infoerror () {
			if (this.error)
				if(this.error.value){
					var config = {};
					config.timeout =  5000;
					config.status = "danger";
					UIkit.notification('A Ocurrido un Error ', config);
					return this.error.value
				}
			return false
		},
		infoloadingform () {
			if (this.loading)
				if(this.loading.value){
					return this.loading.value
				}
			return false

		},
		infoerrorform () {
			if (this.status.type=="ERROR"){
				return this.status			
			}
			return false

		},
		tempUsers () {
			let statuses = ['active', 'disabled'];
			let users = [];
			for (let i = 0; i < 8; i++) {
				users.push({
					id: uniqueID(),
					fName: first(),
					lName: last(),
					phone: phone(),
					email: email(),
					status: statuses[Math.floor(Math.random()*statuses.length)],
					selected: false
				})
			}
			return users;
		},
		tempPlugins () {
			let statuses = ['active', 'disabled'];
			let plugins = [];
			for (let i = 0; i < 6; i++) {
				plugins.push({
					id: uniqueID(),
					name: 'Plugin Name ' + (i + 1),
					version: 'ver. ' + floating({ min: 1, max: 4, fixed: 1 }),
					description: sentence({ words: 20 }),
					status: statuses[Math.floor(Math.random()*statuses.length)],
					selected: false
				})
			}
			return plugins;
		},
		columns () {
			return [
				{
					label: 'Codigo',
					field: 'node.colorCodigo',
					sortable: true,
					sortFn: this.Sort,
					tdClass: 'uk-text-center uk-text-nowrap'
				},
				{
					label: 'Nombre',
					field: 'node.colorNombre',
					tdClass: 'uk-text-center',
					filterOptions: {
						styleClass: 'uk-form-width-large',
						enabled: true
					}

				},
				{
					label: 'Codigo Rndc',
					field: 'node.colorCodigoMinisterio',
					
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Usuario',
					field: 'node.usuarioCodigo',
					filterOptions: {
						styleClass: 'uk-form-width-small',
						enabled: true
					}
				},
				{
					label: 'Created On',
					field: 'node.colorFechacreacion',
					type: 'date',
					dateInputFormat: 'yyyy-MM-dd',
					dateOutputFormat: 'yyyy-MM-dd',
					tdClass: 'uk-text-nowrap uk-text-left'
				},
				{
					label: 'Modified On',
					field: 'node.colorFechamodificacion',
					type: 'date',
					dateInputFormat: 'yyyy-MM-dd',
					dateOutputFormat: 'yyyy-MM-dd',
					tdClass: 'uk-text-nowrap uk-text-left'
				},
				{
					label: 'Actions',
					field: 'actions',
					
				}
			]
		},
	},
	async mounted () {
		this.$nextTick(() => {
			this.tempUsers.forEach(obj => {
				this.settings.users.push(obj)
			});
			this.tempPlugins.forEach(obj => {
				this.settings.plugins.push(obj)
			});
		})
		await this.onLoad();
	},
	methods: {
		async onLoad () {
			await this.DesactivarModales();
			await this.ArregloBasicEstado();
			await this.ArregloBasicArea();
			await this.ArregloBasicCentroCajaCosto();
			await this.ArregloBasicCliente();
			await this.ArregloBasicGrupo();
			await this.ArregloBasicBodega();
		},
		ArregloBasicEstado () {
			//ESTADO
			const GET_ESTADO = gql`
				query QUERY ($codigo: Float, $nombre: String, $modulo: Int, $estado: String) {
					allEstado(estadoCodigo: $codigo, estadoNombre: $nombre, moduloCodigo: $modulo, estadoVisible: $estado){
						edges{
							node{
								estadoCodigo
								estadoNombre
								moduloCodigo
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_ESTADO, 
				{
					modulo: (17),
					estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allEstado.edges.forEach(obj => {
					this.basicEstado.push({ id: obj.node.estadoCodigo, text: obj.node.estadoNombre },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con estados. '+value.allEstado.edges.length+' Registros', config);
			});
		},
		ArregloBasicArea () {
			//Area
			const GET_AREA = gql`
				query QUERY ($codigo: Float, $nombre: String) {
					allArea(areaCodigo: $codigo, areaNombre: $nombre){
						edges{
							node{
								areaCodigo
								areaNombre
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_AREA, 
				{
					//modulo: (17),
					//estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allArea.edges.forEach(obj => {
					this.basicArea.push({ id: obj.node.areaCodigo, text: obj.node.areaNombre },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con areas. '+value.allArea.edges.length+' Registros', config);
			});
		},
		ArregloBasicCentroCajaCosto () {
			//CentroCaja y costos
			const GET_CentroCaja = gql`
				query QUERY ($codigo: Float, $nombre: String) {
					allCentrocosto(cencosCodigo: $codigo, cencosNombre: $nombre){
						edges{
							node{
								cencosCodigo
								cencosNombre
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_CentroCaja, 
				{
					//modulo: (17),
					//estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			let options = [];

			watch(result, value => {
				value.allCentrocosto.edges.forEach(obj => {
					this.basicCentroCaja.push({ id: obj.node.cencosCodigo, text: obj.node.cencosNombre },);
					this.basicCentroCosto.push({ id: obj.node.cencosCodigo, text: obj.node.cencosNombre },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con centro de costo. '+value.allCentrocosto.edges.length+' Registros', config);
			});

		},
		ArregloBasicCliente () {
			//Cliente
			const GET_CLIENTE = gql`
				query QUERY ($codigo: Float, $nombre: String) {
					allCliente(clienteCodigo: $codigo, clienteNombre1: $nombre){
						edges{
							node{
								clienteCodigo
								clienteNombre1
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_CLIENTE, 
				{
					//modulo: (17),
					//estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allCliente.edges.forEach(obj => {
					this.basicCliente.push({ id: obj.node.clienteCodigo, text: obj.node.clienteNombre1 },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con clientes. '+value.allCliente.edges.length+' Registros', config);
			});
		},
		ArregloBasicGrupo () {
			//Grupo
			const GET_GRUPO = gql`
				query QUERY ($codigo: Float, $nombre: String) {
					allGrupo(grupoCodigo: $codigo, grupoNombre: $nombre){
						edges{
							node{
								grupoCodigo
								grupoNombre
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_GRUPO, 
				{
					//modulo: (17),
					//estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allGrupo.edges.forEach(obj => {
					this.basicGrupo.push({ id: obj.node.grupoCodigo, text: obj.node.grupoNombre },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con grupos. '+value.allGrupo.edges.length+' Registros', config);
			});

		},
		ArregloBasicBodega () {
			//BODEGA
			const GET_BODEGA = gql`
				query QUERY ($codigo: Float, $nombre: String) {
					allBodega(bodegaCodigo: $codigo, bodegaNombre: $nombre){
						edges{
							node{
								bodegaCodigo
								bodegaNombre
							}
						}	
					}	
				}
				`;
			let {result, loading, error }  =  provideApolloClient(this.$apollo)(() => useQuery(GET_BODEGA, 
				{
					//modulo: (17),
					//estado: ("SI"),
				},
				{
					errorPolicy: 'all',
					fetchPolicy: 'no-cache'
				}));
			
			this.result=result;
			this.loading=loading;
			this.error=error;

			watch(result, value => {
				value.allBodega.edges.forEach(obj => {
					this.basicBodega.push({ id: obj.node.bodegaCodigo, text: obj.node.bodegaNombre },);
				});

				var config = {};
				config.timeout =  3000;
				config.status = "success";
				UIkit.notification('Consulta Ejecutada Correctamente con bodegas. '+value.allBodega.edges.length+' Registros', config);
			});

		},
		DesactivarModales () {
			//UIkit.modal('#process').hide();
		},
		async submitForm (e, operation) {
			e.preventDefault();
			this.$v.$touch();
			if (!this.$v.$invalid) {
				this.submitStatus = 'ERROR';
				var config = {};
				config.timeout =  3000;
				config.status = "warning";
				UIkit.notification('Error', config);
			} else {
				this.submitStatus = 'OK';
				
				if(operation=="CREATE"){
					await this.create();
				}		
				
			} 
		},
		async create () {
			//REALIZAR MUTACION DE USUARIOS EN USUARIOS 
			this.status.type='';
			//CREATE USER
			const SAVE_USER = gql`
				mutation createUsuario($name: String!, $usuarioLogin: String!, $usuarioClave: String!, $ciudadCodigo: Int!, $usuarioCedula: String!, $estadoCodigo: Int!, $usuarioAutoriza: String!, $email: String!, $usuarioCodigoCreacion: Int!, $usuarioTipomenu: String!, $usuarioTipo: Int!){
					createUsuario(name: $name, usuarioLogin: $usuarioLogin, usuarioClave: $usuarioClave, ciudadCodigo: $ciudadCodigo, usuarioCedula: $usuarioCedula, estadoCodigo: $estadoCodigo, usuarioAutoriza: $usuarioAutoriza, email: $email, usuarioCodigoCreacion: $usuarioCodigoCreacion, usuarioTipomenu: $usuarioTipomenu, usuarioTipo: $usuarioTipo ) {
						node{
							id
							name
							usuarioLogin
							usuarioClave
							ciudadCodigo
							usuarioCedula
							estadoCodigo
							usuarioAutoriza
							email
							usuarioCodigoCreacion
							usuarioTipomenu
							usuarioTipo
							usuarioFechacreacion
							usuarioFechamodificacion
						}
					}
				}
			`;

			let {mutate: createUsuario, loading: userLoading, error: userError, onDone, onError}  =   provideApolloClient(this.$apollo)(() => useMutation(SAVE_USER));

			createUsuario({
				name: this.$data.name.toUpperCase(),
				usuarioLogin: this.$data.usuarioLogin.toUpperCase(),
				usuarioClave: this.$data.password,				
				ciudadCodigo: 8401,
				usuarioCedula: this.$data.cedula,
				estadoCodigo: this.$data.estado,
				usuarioAutoriza: this.$data.autoriza,
				email: this.$data.email,
				usuarioCodigoCreacion: 1,
				usuarioTipomenu: "MENU_1",
				usuarioTipo: 0
			})
			
			this.loading=userLoading;
			this.submitStatus="PENDING"

			var config = {};
			config.timeout =  5000;
			
			onDone(result => {
  				this.submitStatus="OK"
				this.status.type="SUCCESS"
				config.status = "success";
				var mensaje = "Se crea el usuario <b>" + result.data.createUsuario.node.name + "</b> correctamente.";
				//UIkit.notification(mensaje, config);

				let grupos = [];
				let elementos_grupos;

				this.$data.grupo.forEach(element => {
					elementos_grupos = {};
					elementos_grupos.usuarioCodigo = result.data.createUsuario.node.id;
					elementos_grupos.grupoCodigo = element;
					grupos.push(elementos_grupos);
				});

				console.log("grupos");
				console.log(grupos);
				this.asignarGrupoUsuario(grupos);
			})
			
			onError(error => {
  				logErrorMessages(error);
				this.submitStatus="CORREGIR";
				this.status.type="ERROR";
				this.status.message=userError.value;
				config.status = "danger";
				UIkit.notification('No se creo el registro, Por favor corrija e intente nuevamente.', config);
			})
		},
		toggleAllUsers (state) {
			this.settings.users.forEach((k, index) => {
				this.settings.users[index].selected = state
			});
		},
		toggleUser (value) {
			let users = this.settings.users.map((k) => {
				return k.selected
			});
			let someChecked = users.some(cb => cb === true);
			let allChecked = users.every(cb => cb === true);
			if (allChecked) {
				this.userTable.checkAll = true;
				this.userTable.checkAllInd = false
			} else if (someChecked) {
				this.userTable.checkAllInd = true
			} else {
				this.userTable.checkAll = false;
				this.userTable.checkAllInd = false
			}
		},
		toggleAllPlugins (state) {
			this.settings.plugins.forEach((k, index) => {
				this.settings.plugins[index].selected = state
			});
		},
		togglePlugin (value) {
			let plugins = this.settings.plugins.map((k) => {
				return k.selected
			});
			let someChecked = plugins.some(cb => cb === true);
			let allChecked = plugins.every(cb => cb === true);
			if (allChecked) {
				this.pluginTable.checkAll = true;
				this.pluginTable.checkAllInd = false
			} else if (someChecked) {
				this.pluginTable.checkAllInd = true
			} else {
				this.pluginTable.checkAll = false;
				this.pluginTable.checkAllInd = false
			}
		},
		togglePluginStatus (plugin) {
			let status = plugin.status;
			if(status === 'active') {
				plugin.status = 'disabled'
			}
			if(status === 'disabled') {
				plugin.status = 'active'
			}
		},
		openDialog (type) {
			var self = this;
			if(type === 'dialog') {
				UIkit.modal.dialog('<p class="uk-modal-body">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Cupiditate enim consequuntur, saepe mollitia aliquam quia, delectus cum, nobis quisquam ipsam rerum excepturi repellendus explicabo perspiciatis dolor accusantium! Voluptates, asperiores rerum.</p>');
			}
			if(type === 'alert') {
				UIkit.modal.alert('UIkit alert!').then(function () {
					console.log('Alert closed.')
				})
			}
			if(type === 'confirm') {
				UIkit.modal.confirm('UIkit confirm!').then(function () {
					console.log('Confirmed.')
				}, function () {
					console.log('Rejected.')
				})
			}
			if(type === 'prompt') {
				/*UIkit.modal.prompt('Name:', self.promptName).then(function (name) {
					// console.log('Prompted: ', name)
					self.promptName = name
				})*/
				console.log("entre en modal");

				UIkit.modal('#process').show();
			}
		}, 
		resetFieldSubmit () {
			this.usuarioLogin = '';
			this.name = '';
			this.password = '';
			this.repeatPassword = '';
			this.email = '';
			this.cedula = '';
			this.ciudad = '';
			this.estado = '';
			this.autoriza = '';
			this.centroCosto = '';
			this.grupo = '';
		},
		asignarGrupoUsuario (grupos) {
			this.status.type='';
			console.log("entre en asignacion");
			//CREATE USER
			const SAVE_USER_GROUP = gql`
				mutation createUsuariogrupo($usuarioCodigo: Int!, $grupoCodigo: Int!){
					createUsuariogrupo(usuarioCodigo: $usuarioCodigo, grupoCodigo: $grupoCodigo ) {
						node{
							usuarioCodigo
							grupoCodigo
						}
					}
				}
			`;

			createUsuariogrupo = grupos;
			
			let {mutate: createUsuariogrupo, loading: userLoading, error: userError, onDone, onError}  =   provideApolloClient(this.$apollo)(() => useMutation(SAVE_USER_GROUP));

			

			/*
			createUsuariogrupo({
				name: this.$data.name.toUpperCase(),
				usuarioLogin: this.$data.usuarioLogin.toUpperCase(),
				usuarioClave: this.$data.password,				
				ciudadCodigo: 8401,
				usuarioCedula: this.$data.cedula,
				estadoCodigo: this.$data.estado,
				usuarioAutoriza: this.$data.autoriza,
				email: this.$data.email,
				usuarioCodigoCreacion: 1,
				usuarioTipomenu: "MENU_1",
				usuarioTipo: 0
			})*/
			
			this.loading=userLoading;
			this.submitStatus="PENDING"

			var config = {};
			config.timeout =  5000;
			
			onDone(result => {
				console.log("PRUEBA");
  				this.submitStatus="OK"
				this.status.type="SUCCESS"
				config.status = "success";
				var mensaje = "Se crea el usuario <b></b> correctamente.";
				UIkit.notification(mensaje, config);
				this.resetFieldSubmit();
			})
			
			onError(error => {
  				logErrorMessages(error);
				this.submitStatus="CORREGIR";
				this.status.type="ERROR";
				this.status.message=userError.value;
				config.status = "danger";
				UIkit.notification('No se creo el registro, Por favor corrija e intente nuevamente.', config);
			})
		}
	}, 
	validations: {
		usuarioLogin: {
			required
		},
		name: {
			required
		}, 
		password: {
			required,
			minLength: minLength(6)
		},
		repeatPassword: {
			sameAsPassword: sameAs('password')
		}, 
		notes: {
			required
		}, 
		cedula: {
			required,
			minLength: minLength(7),
			maxLength: maxLength(10)
		}, 
		ciudad: {
			required
		}, 
		estado: {
			required
		}, 
		autoriza: {
			required
		}, 
		centroCosto: {
			required
		}, 
		grupo: {
			required
		}, 
		email: {
			required
		}, 
	},
}
</script>

<style lang="scss">
	@import '~scss/vue/_pretty_checkboxes';
</style>
